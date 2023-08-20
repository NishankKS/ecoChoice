# ecoChoice - An Intelligent Recommendation System  

## Deliverables  
Model Design and Implementation: To develop a robust machine learning model that generates personalized product rankings based on user preferences, past interactions, product popularity, and user similarity.  

Ranking Generation Mechanism: To design a ranking generation mechanism that takes user and product attributes as input and outputs personalized rankings for each user within specific product categories.  

Evaluation Metrics: To establish legitimate evaluation metrics like coverage, RMSE to assess the accuracy and relevance of the generated rankings against user interactions.  

Technical Documentation: Provide well-documented technical details outlining the workflow, data preprocessing, model training, and ranking generation process.  


## Proposed approach

The dataset contains entities of user_id, product_id, user_rating and time_stamp. These records encompass different categories such as Beauty products, appliances, cell phones and accessories and magazine subscriptions.

The recommendation type used is model-based collaborative filtering method that builds predictive models using user-item interaction data to make recommendations, leveraging techniques like matrix factorization to capture latent factors and generate personalized suggestions.

The ratings given by the users to particular products and identified and serve as the main criteria to determine the similarity between items.

The existing user_id of the user is taken as input and the highly rated products by the user obtained from the past purchase history of the user which is fed into the model.

Matrix factorization is used to uncover latent patterns and relationships within user-item interaction data. A correlation matrix is constructed for the same.

Items having correlation values greater than 0.65 are recommended to the user.  

## System Workflow  

![image](https://github.com/dheerajgajula02/flipkart_grid/assets/80829447/f152621d-632f-45ef-a885-59d8a6ed55a2)

| End points  | methods | header |
| ------------- | ------------- | -------|
| order_list  | get  | {"user_id": [user_id]}
| high_rating  | get  | {"user_id": [user_id]}
| meta_data | get | {"user_id": [user_id]}

## usage
- The purpose of order_list is to list all the orders by the user
- high_rating returns the highest rated product of the user
- meta_data returns the meta data of the products that the specific user bought previously 

## Evaluation Metrics

Coverage: Coverage is the percent of items in the training data the model is able to recommend on a test set. In our solution, the popularity recommender has 0.05% coverage, the collaborative filter is able to recommend 8.42% of the items it was trained on.

RMSE is an evaluation metric in recommendation systems that measures the average squared difference between predicted and actual ratings, providing a measure of prediction accuracy. In our solution, RMSE is about 0.1893

## Use-cases  
P0: Personalized beauty recommendations optimize skincare and makeup choices by tailoring products and routines to individual needs, preferences, and changing seasons.

P1: Smart cell phone upgrades include personalized device suggestions and accessory recommendations, considering usage patterns, preferences, and future trends for a seamless and tailored experience.

P2: Personalized magazine subscriptions curate content through interest-aligned recommendations, diverse genre exploration, adaptive selection, curated collections, and a balanced mix of print and digital formats.

P3: Personalized appliance recommendations optimize efficiency, convenience, and home setups by suggesting energy-saving options, smart kitchen gadgets, curated bundles, tailored entertainment setups, and maintenance guidance.

P4: Personalized e-commerce recommendations leverage user behavior for tailored suggestions, boosting sales and customer satisfaction through cross-selling and upselling strategies.

## Advantages

The solution has the ability to recommend a larger number of items to a larger number of users, compared to other methods like memory based approach. They have large coverage, even when working with large sparse matrices.

The solution offers precise relevance and individualized experiences, driving user engagement, boosting sales through cross-selling, and facilitating efficient decision-making based on tailored item rankings through personalized recommendations.

Cross-selling involves suggesting complementary items to what the user is interested in, increasing their purchase value. Upselling highlights higher-tier or upgraded options, encouraging users to consider premium alternatives, thus enhancing revenue potential.

## Limitations
Cold Start Problem: New users or items with limited interaction history pose a challenge for the solution, as there is not enough data to provide meaningful personalized suggestions.

Narrow Scope: Limited categories constrain the variety of recommendations, potentially leading to repetitive or less diverse suggestions for users.

Limited User Preferences: With fewer categories, the system struggles to capture complex and nuanced user preferences, resulting in less accurate recommendations.

Ineffective for Diverse Audiences: If the available categories do not align well with the interests of a diverse user base, the system might struggle to cater to various preferences.

## Future Scope
Real-time Personalization: Incorporating real-time data such as user location, weather conditions, and browsing behavior to provide even more relevant and timely product recommendations.

Integration of User Feedback: To develop mechanisms to gather and incorporate user feedback on recommended products, allowing the system to continuously refine its suggestions.

Context-Aware Recommendations: To consider user context such as time of day, device being used, and recent interactions to offer recommendations that align with specific situations.

Collaborative Filtering Refinements: Refining collaborative filtering models by incorporating factors like user trust levels, frequency of interactions, and network influence.

Customization Interfaces: Developing user-friendly interfaces that allow users to fine-tune their preferences and refine their personalized recommendations manually.

Multi-Domain Recommendations:  Applying the personalized ranking system to new domains and industries, leveraging its capabilities for diverse sectors.

##Steps to run this project:  
STEP 1: Clone the GitHub repository.  
STEP 2: Move to folder streamlit_front_end.  
STEP 3: Run the code provided below in the terminal of the project folder.

Install the requirements:
```
pip install -r requirements.txt
```

Run the app:
```
streamlit run recommender.py
```







