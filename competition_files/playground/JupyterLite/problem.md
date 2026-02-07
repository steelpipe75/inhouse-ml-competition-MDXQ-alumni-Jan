# タスク概要

## 分類タスクの説明

本コンペティションでは、与えられた特徴量 `feature_0`, `feature_1` から目的変数 `target` を予測するクラス分類問題です。  
`target` は`0`, `1`のいずれかのクラスに属します。

- 入力：
  - `id`, `feature_0`, `feature_1`, `target` からなる訓練用データ（`train.csv`）
  - `id`, `feature_0`, `feature_1` からなるテストデータ（`test.csv`）
- 出力：
  - 各 `id` がクラス`1`である確率の予測値 `cls1_probability`（`sample_submission.csv` 形式）
- 評価指標：
  - AUC
