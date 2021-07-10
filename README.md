# optiver-kaggle
A repo for the Optiver Realized Volatility Prediction Kaggle Competition

1. To get started with the notebook, first install the requirements from the `requirements.txt`. This can be done by uncommenting the first cell and running it or by running the following command in your terminal:

    `pip install -r requirements.txt`

2. Run the next cell to generate a `optiver-kaggle.env` file. Please be sure to include the follwing in the file:

    ```
    KAGGLE_USERNAME=datadinosaur
    KAGGLE_KEY=xxxxxxxxxxxxxx
    ```
    
3. Run the 3rd and 4th cells to source the dataset. If the `./data` directory already exists and is not empty the script will do nothing. If the `./data` directory already exists and is empty then the script will download the files into that directory. Otherwise, the script will create the directory and downloand the files to that directory.

From here you can continue to run the notebook to process the files in the `./data` directory.