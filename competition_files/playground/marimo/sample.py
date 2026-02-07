# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo>=0.19.9",
# ]
# ///
import marimo

__generated_with = "0.19.4"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    import micropip
    return (micropip,)


@app.cell
async def _(micropip):
    await micropip.install("polars")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 機械学習コンペ 分類問題 サンプルノートブック
    """)
    return


@app.cell
def _():
    import polars as pl
    import numpy as np
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import roc_curve, roc_auc_score
    from matplotlib import pyplot as plt
    return (
        LogisticRegression,
        pl,
        plt,
        roc_auc_score,
        roc_curve,
        train_test_split,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## コンペ配布データ読み込み
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 学習用データ読み込み
    """)
    return


@app.cell
def _(mo):
    train_csv_path = mo.notebook_location() / "public" / "data" / "train.csv"
    train_csv_path
    return (train_csv_path,)


@app.cell
def _(pl, train_csv_path):
    train_df = pl.read_csv(str(train_csv_path))
    train_df
    return (train_df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 評価用データ読み込み
    """)
    return


@app.cell
def _(mo):
    test_csv_path = mo.notebook_location() / "public" / "data" / "test.csv"
    test_csv_path
    return (test_csv_path,)


@app.cell
def _(pl, test_csv_path):
    test_df = pl.read_csv(str(test_csv_path))
    test_df
    return (test_df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### サンプル投稿ファイル読み込み
    """)
    return


@app.cell
def _(mo):
    submit_csv_path = mo.notebook_location() / "public" / "data" / "sample_submission.csv"
    submit_csv_path
    return (submit_csv_path,)


@app.cell
def _(pl, submit_csv_path):
    submit = pl.read_csv(str(submit_csv_path))
    submit
    return (submit,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 前処理
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 説明変数、目的変数に分割
    """)
    return


@app.cell
def _(train_df):
    X = train_df[["feature_0", "feature_1"]]
    y = train_df["target"]
    return X, y


@app.cell
def _(X):
    X
    return


@app.cell
def _(y):
    y
    return


@app.cell
def _(test_df):
    X_test = test_df[["feature_0", "feature_1"]]
    return (X_test,)


@app.cell
def _(X_test):
    X_test
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 訓練用データ、検証用データに分割
    """)
    return


@app.cell
def _(X, train_test_split, y):
    X_train, X_eval, y_train, y_eval = train_test_split(X, y)
    return X_eval, X_train, y_eval, y_train


@app.cell
def _(X_train):
    X_train
    return


@app.cell
def _(y_train):
    y_train
    return


@app.cell
def _(X_eval):
    X_eval
    return


@app.cell
def _(y_eval):
    y_eval
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## モデルを訓練
    """)
    return


@app.cell
def _(LogisticRegression):
    model = LogisticRegression()
    return (model,)


@app.cell
def _(X_train, model, y_train):
    model.fit(X_train, y_train)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 訓練済みモデルによる予測（検証用データ）
    """)
    return


@app.cell
def _(X_eval, model):
    y_pred_eval = model.predict_proba(X_eval)
    return (y_pred_eval,)


@app.cell
def _(pl, y_pred_eval):
    y_pred_eval_df = pl.DataFrame(y_pred_eval)
    return (y_pred_eval_df,)


@app.cell
def _(y_pred_eval_df):
    y_pred_eval_df
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    予測精度の可視化
    """)
    return


@app.cell
def _(roc_auc_score, roc_curve, y_eval, y_pred_eval_df):
    fpr, tpr, thresholds  = roc_curve(y_eval, y_pred_eval_df["column_1"])
    auc = roc_auc_score(y_eval, y_pred_eval_df["column_1"])
    return auc, fpr, tpr


@app.cell
def _(fpr, plt, tpr):
    plt.plot(fpr, tpr, marker='o')
    plt.xlabel('FPR: False positive rate')
    plt.ylabel('TPR: True positive rate')
    plt.grid()

    plt.gca()
    return


@app.cell
def _(auc):
    auc
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 訓練済みモデルによる予測（評価用データ）
    """)
    return


@app.cell
def _(X_test, model):
    y_pred_test = model.predict_proba(X_test)
    return (y_pred_test,)


@app.cell
def _(pl, y_pred_test):
    y_pred_test_df = pl.DataFrame(y_pred_test)
    return (y_pred_test_df,)


@app.cell
def _(y_pred_test_df):
    y_pred_test_df
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 採点用投稿ファイル作成
    """)
    return


@app.cell
def _(submit, y_pred_test_df):
    my_submit = submit.with_columns(
        y_pred_test_df["column_1"].alias("cls1_probability")
    )
    return (my_submit,)


@app.cell
def _(my_submit):
    my_submit
    return


@app.cell
def _(my_submit):
    my_submit.write_csv("submit.csv")
    return


if __name__ == "__main__":
    app.run()
