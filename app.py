{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "48ae2631-23fd-4a8c-bc37-766ccd44da0f",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7ffc0b4d-73b6-454d-ba3d-69cf0be80124",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "from sklearn.preprocessing import StandardScaler\n",
    "from sklearn.impute import SimpleImputer\n",
    "from sklearn.cluster import KMeans\n",
    "from sklearn.metrics import silhouette_score\n",
    "\n",
    "st.title(\"Clustering Analysis App\")\n",
    "\n",
    "# File Upload\n",
    "uploaded_file = st.file_uploader(\"Upload your Excel file\", type=\"xlsx\")\n",
    "if uploaded_file:\n",
    "    try:\n",
    "        # Read and display data\n",
    "        data = pd.read_excel(uploaded_file)\n",
    "        st.write(\"### Raw Data\", data.head())\n",
    "\n",
    "        # Preprocess Data\n",
    "        numeric_cols = data.select_dtypes(include=[\"number\"]).columns\n",
    "        imputer = SimpleImputer(strategy=\"mean\")\n",
    "        data[numeric_cols] = imputer.fit_transform(data[numeric_cols])\n",
    "\n",
    "        # Scale Data\n",
    "        scaler = StandardScaler()\n",
    "        scaled_data = scaler.fit_transform(data[numeric_cols])\n",
    "\n",
    "        # Clustering\n",
    "        n_clusters = st.slider(\"Select Number of Clusters\", 2, 10, 3)\n",
    "        kmeans = KMeans(n_clusters=n_clusters, random_state=42)\n",
    "        data[\"Cluster\"] = kmeans.fit_predict(scaled_data)\n",
    "        st.write(\"### Clustered Data\", data)\n",
    "\n",
    "        # Visualize Clusters\n",
    "        fig, ax = plt.subplots()\n",
    "        sns.scatterplot(\n",
    "            x=scaled_data[:, 0], y=scaled_data[:, 1], hue=data[\"Cluster\"], palette=\"viridis\", ax=ax\n",
    "        )\n",
    "        plt.title(\"Clusters Visualization\")\n",
    "        st.pyplot(fig)\n",
    "\n",
    "        # Silhouette Score\n",
    "        silhouette = silhouette_score(scaled_data, data[\"Cluster\"])\n",
    "        st.write(f\"Silhouette Score: {silhouette:.2f}\")\n",
    "\n",
    "    except Exception as e:\n",
    "        st.error(f\"An error occurred: {e}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "343d9db0-768c-4429-bb8d-e4b6a3f7ce36",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d4569372-bec3-4160-bc08-6b12ed9dd9c2",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3ecd68a3-02a3-4bf4-baf0-875516e417f1",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
