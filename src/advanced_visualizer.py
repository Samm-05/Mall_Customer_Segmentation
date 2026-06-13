import pandas as pd

from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

import plotly.express as px


def create_pca(df, X, labels):

    pca = PCA(
        n_components=2,
        random_state=42
    )

    transformed = pca.fit_transform(
        X
    )

    pca_df = pd.DataFrame(
        {
            "PC1": transformed[:, 0],
            "PC2": transformed[:, 1],
            "Cluster": labels
        }
    )

    return pca_df


def create_tsne(df, X, labels):

    tsne = TSNE(
        n_components=2,
        random_state=42,
        perplexity=30
    )

    transformed = tsne.fit_transform(
        X
    )

    tsne_df = pd.DataFrame(
        {
            "TSNE1": transformed[:, 0],
            "TSNE2": transformed[:, 1],
            "Cluster": labels
        }
    )

    return tsne_df


def pca_chart(pca_df):

    fig = px.scatter(
        pca_df,
        x="PC1",
        y="PC2",
        color="Cluster",
        title="PCA Cluster Visualization"
    )

    return fig


def tsne_chart(tsne_df):

    fig = px.scatter(
        tsne_df,
        x="TSNE1",
        y="TSNE2",
        color="Cluster",
        title="t-SNE Cluster Visualization"
    )

    return fig