# Dimension Collaboration Log Application

<img width="746" alt="dimension_logapp_screenshot" src="https://github.com/devindatt/dimension_smart_action/assets/42626142/3d5dc167-dcd9-4baf-972b-f7bf0196a18c">

## Overview

The Dimension Collaboration Log Application is a Streamlit-based web application designed to enhance team collaboration by logging user inputs, categorizing them, and recommending relevant tools or actions. This application leverages the power of GPT-3.5 for natural language processing and decision-making, providing smart recommendations based on user logs.

## Features

Log Submission: Users can submit logs about their development issues or observations.
Automatic Categorization: The app categorizes each log into a specific development issue category using a custom-built AI model.
Tool Recommendation: Based on the category, it recommends the most suitable tools or actions.


## Files Description

- dim_smart_feature.py: Main application file with Streamlit UI components and application logic.
- genai_recommendations.py: Contains functions to get recommendations for categories and tools using the LangChain and OpenAI's GPT-3.5 model.
- external_items.py: Includes predefined lists of log items, possible outputs, categories, and tools.


## Prerequisites

- Python 3.x
- Streamlit
- OpenAI API Key


## Installation

Clone the repository:
bash
git clone [repository URL]
<img width="695" alt="clone_repo" src="https://github.com/devindatt/dimension_smart_action/assets/42626142/165e7715-168b-4813-b2fb-dfe09e562d93">

Install required packages:
pip install -r requirements.txt
<img width="687" alt="install_requirements" src="https://github.com/devindatt/dimension_smart_action/assets/42626142/942cb4db-a887-4795-8c72-79ebe3c9b154">

## Usage

Set your OpenAI API key as an environment variable:

export OPENAI_API_KEY='your_api_key_here'
<img width="690" alt="install_openai_key" src="https://github.com/devindatt/dimension_smart_action/assets/42626142/3e0c81b1-fca5-4288-8367-154a9d8e3b68">

Run the Streamlit app:
streamlit run dim_smart_feature.py
<img width="686" alt="run_streamlit_app" src="https://github.com/devindatt/dimension_smart_action/assets/42626142/1288708c-d8d2-4701-9066-96213b9bee92">

## Contributing

Contributions to improve the application are welcome. Please follow the standard fork-and-pull request workflow.

## License

Apache License - free to use


Contact

For any queries or suggestions, please contact Devin Datt at devindatt@sonarai.io
