# generate_classification_data.py
from sklearn.datasets import make_gaussian_quantiles
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

def generate_and_save_data():
    """
    scikit-learnのmake_gaussian_quantilesを使って2クラス分類問題のデータセットを生成し、
    訓練データとテストデータに分割してCSVファイルとして保存する。
    """
    # 2クラス分類問題のデータセットを生成
    # n_samples: サンプル数 (1100)
    # n_features: 説明変数の数 (2)
    # n_classes: クラス数 (2)
    # random_state: 再現性のためのシード値
    X, y = make_gaussian_quantiles(n_samples=1100, n_features=2, n_classes=2, random_state=42)

    # データを訓練用とテスト用に分割
    # テストデータのサイズを100に指定
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=100, random_state=42, stratify=y)

    print("データ分割後の形状:")
    print(f"訓練データ (X_train) の形状: {X_train.shape}")
    print(f"テストデータ (X_test) の形状: {X_test.shape}")
    print(f"訓練データ (y_train) の形状: {y_train.shape}")
    print(f"テストデータ (y_test) の形状: {y_test.shape}")

    # 訓練データをDataFrameに変換してCSVとして保存
    train_df = pd.DataFrame(X_train)
    train_df['target'] = y_train
    train_df.to_csv('train.csv')
    print("\n訓練データを 'train.csv' として保存しました。")

    # テストデータ（説明変数）をDataFrameに変換してCSVとして保存
    test_df = pd.DataFrame(X_test)
    test_df.to_csv('test.csv')
    print("テストデータの説明変数を 'test.csv' として保存しました。")

    # テストデータ（正解ラベル）をDataFrameに変換してCSVとして保存
    ground_truth_df = pd.DataFrame(y_test)
    ground_truth_df.to_csv('ground_truth.csv')
    print("テストデータの正解ラベルを 'ground_truth.csv' として保存しました。")


if __name__ == "__main__":
    generate_and_save_data()

