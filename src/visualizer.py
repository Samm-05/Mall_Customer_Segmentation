import plotly.express as px
from sklearn.decomposition import PCA
import pandas as pd


def create_pca_dataframe(X, labels):

    pca = PCA(
        n_components=2
    )

    transformed = pca.fit_transform(X)

    pca_df = pd.DataFrame(
        {
            "PC1": transformed[:, 0],
            "PC2": transformed[:, 1],
            "Cluster": labels
        }
    )

    return pca_df


def pca_plot(pca_df):

    fig = px.scatter(
        pca_df,
        x="PC1",
        y="PC2",
        color=pca_df["Cluster"].astype(str),
        title="PCA Cluster Visualization"
    )

    return fig