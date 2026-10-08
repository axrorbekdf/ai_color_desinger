import json
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sqlalchemy.orm import Session

from app.models.feedback import UserFeedback, MLExperiment
from app.models.analysis import ColorRecommendation

def train_and_evaluate_ml_model(db: Session, model_type: str):
    # 1. Dataset loading and feature extraction
    feedbacks = db.query(UserFeedback).all()
    
    if len(feedbacks) < 10:
        return {"error": "Not enough data to train ML models. Minimum 10 feedbacks required."}
        
    X = []
    y = []
    
    for fb in feedbacks:
        rec = db.query(ColorRecommendation).filter(ColorRecommendation.id == fb.recommendation_id).first()
        if rec:
            # Features: harmony_score, mood_score, compatibility_score
            X.append([rec.harmony_score, rec.mood_score, rec.compatibility_score])
            # Target: whether the user accepted it or rated it highly
            y.append(1 if fb.accepted or fb.rating >= 4 else 0)
            
    if len(set(y)) < 2:
        return {"error": "Data must contain both positive (accepted/rated >= 4) and negative examples to train."}

    # 2. Train/test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # 3. Model Selection
    if model_type == "Random Forest":
        clf = RandomForestClassifier(n_estimators=100, random_state=42)
    elif model_type == "KNN":
        clf = KNeighborsClassifier(n_neighbors=3)
    elif model_type == "SVM":
        clf = SVC(kernel="linear", random_state=42)
    elif model_type == "Logistic Regression":
        clf = LogisticRegression(random_state=42)
    else:
        return {"error": "Invalid model_type"}
        
    # 4. Training
    clf.fit(X_train, y_train)
    
    # 5. Prediction
    y_pred = clf.predict(X_test)
    
    # 6. Evaluation
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred, zero_division=0)
    rec = recall_score(y_test, y_pred, zero_division=0)
    f1 = f1_score(y_test, y_pred, zero_division=0)
    
    # Save experiment results to DB
    experiment = MLExperiment(
        model_type=model_type,
        accuracy=acc,
        precision=prec,
        recall=rec,
        f1_score=f1,
        parameters=json.dumps(clf.get_params())
    )
    db.add(experiment)
    db.commit()
    db.refresh(experiment)
    
    return {
        "model_type": model_type,
        "accuracy": acc,
        "precision": prec,
        "recall": rec,
        "f1_score": f1
    }
