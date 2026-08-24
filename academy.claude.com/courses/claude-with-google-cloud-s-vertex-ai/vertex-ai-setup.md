<!-- source: https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/vertex-ai-setup -->

Lesson 2 of 66 · Claude with Google Cloud's Vertex AIVertex AI Setup

In the next video we will be making a request to Vertex AI in order to call a Claude model. To do so, you need to go through a little bit of setup.

#### Step One: Ensure Anthropic models are enabled in Vertex

* In your browser, navigate to [https://console.cloud.google.com/vertex-ai/dashboard(opens in new tab)](https://console.cloud.google.com/vertex-ai/dashboard)
* In the left hand nav, click on **'Model Garden'**

**![](https://academy.claude.com/assets/media/4ed45039d908471c0140d088a93ecbb9afa9d9e0081a423e573588997739b347.png)**

* In the **'Search models'** box, enter **'Anthropic'**

**![](https://academy.claude.com/assets/media/62117edb2bb3792973deb3ade3a8571192475ae2a840aca9f67e49c20e1bf774.png)**

* Click on the model that you want to use.

#### Step Two: Enable the Model

* Once you've found the model you want to use, you may need to enable it. On the model information page, click the **'Enable'** button
* If you don't see an **'Enable'** button then you already have access to the model

![](https://academy.claude.com/assets/media/6516b221ada00426650856c083ca95a70929d646205545a2283bf5e1d37a1062.png)

#### Step Three: Install the gcloud CLI

If you don't already have the gcloud CLI installed, follow the directions here to install and authenticate with the CLI: [https://cloud.google.com/sdk/docs/install(opens in new tab)](https://cloud.google.com/sdk/docs/install)

#### Step Four: Login and set up authentication with the gcloud CLI

If you have not already logged in to the gcloud CLI, do so by running:

bash

```
gcloud init
gcloud auth login
```

Then, set your project ID and set your default credentials:

bash

```
gcloud config set project YOUR_PROJECT_ID
gcloud auth application-default login
```

That's it! The Anthropic SDK will automatically use these credentials when attempting to access Vertex.
