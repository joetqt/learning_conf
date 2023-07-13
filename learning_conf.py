import logging
import plotly.express as px
# Configure the logging
logging.basicConfig(level=logging.ERROR, format='USER ENTRY: %(asctime)s - %(message)s')
logger = logging.getLogger("error_logger")
conf_records = []

def get_confidence():
    try:
        # Prompt user for input
        number = input("How confident do you feel right now on learning the content above? \n0 - Least confident; 100 - Most confident \nPlease enter an integer between 0 and 100: ")
        # Validate input
        while True:
            try:
                number = int(number)
                if 0 <= number <= 100:
                    break
            except ValueError:
                pass
            number = input("Invalid input. Please try again. \nPlease enter an integer between 0 and 100: ")
        # Intentionally trigger an error
        if int(number) != -9999:
            error_message = f"The integer you entered is: {number}"
            # Add the number to the list
            conf_records.append(number)
            # Log the error message to the centralised error tracking service
            logger.error(error_message)
    except ValueError:
        pass
    
def plot_confidence():
    fig = px.line(y=conf_records, range_y=[0, 100])
    fig.update_layout(
        xaxis_title="Your entries for this session",
        yaxis_title="Your learning confidence input",
        title="Trend of your learning confidence for this session",title_x=0.5)
    fig.show()