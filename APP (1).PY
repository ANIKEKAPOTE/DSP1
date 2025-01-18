{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "354668cc-9dcb-4229-b7ae-60ca96b68ca9",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-01-18 12:54:50.158 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\anike\\anaconda3\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    }
   ],
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
    "# Upload File\n",
    "uploaded_file = st.file_uploader(\"Upload your Excel file\", type=\"xlsx\")\n",
    "if uploaded_file:\n",
    "    data = pd.read_excel(uploaded_file)\n",
    "    st.write(\"### Raw Data\", data.head())\n",
    "\n",
    "    # Handle Missing Data\n",
    "    numeric_cols = data.select_dtypes(include=[\"number\"]).columns\n",
    "    imputer = SimpleImputer(strategy=\"mean\")\n",
    "    data[numeric_cols] = imputer.fit_transform(data[numeric_cols])\n",
    "\n",
    "    # Scale Data\n",
    "    scaler = StandardScaler()\n",
    "    scaled_data = scaler.fit_transform(data[numeric_cols])\n",
    "\n",
    "    # Clustering\n",
    "    n_clusters = st.slider(\"Select Number of Clusters\", 2, 10, 3)\n",
    "    kmeans = KMeans(n_clusters=n_clusters, random_state=42)\n",
    "    data[\"Cluster\"] = kmeans.fit_predict(scaled_data)\n",
    "    st.write(\"### Clustered Data\", data)\n",
    "\n",
    "    # Visualize Clusters\n",
    "    fig, ax = plt.subplots()\n",
    "    sns.scatterplot(\n",
    "        x=scaled_data[:, 0], y=scaled_data[:, 1], hue=data[\"Cluster\"], palette=\"viridis\", ax=ax\n",
    "    )\n",
    "    plt.title(\"Clusters Visualization\")\n",
    "    st.pyplot(fig)\n",
    "\n",
    "    # Silhouette Score\n",
    "    silhouette = silhouette_score(scaled_data, data[\"Cluster\"])\n",
    "    st.write(f\"Silhouette Score: {silhouette:.2f}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "68628ccd-833a-4be7-ae3c-4ba5a19ffb55",
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
