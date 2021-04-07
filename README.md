# dynamic-color-logger


A logger whose colors aren't specific to its levels but rather specified dynamically like so:

my_red_personal_logger = create_personal_logger(color='red')
my_green_personal_logger = create_personal_logger(color='green')

my_red_personal_logger.info('something is happening with this feature')
my_red_personal_logger.warning('something bad is happening with this feature')
my_red_personal_logger.critical('something REALLY bad is happening with this feature')
#all of these messages will be red

my_green_personal_logger.info('something is happening with another feature')
#this message will be green

This is useful when onboarding on large and/or convoluted codebases where the call stack is not obvious from the architecture. In such cases we might want to log different things with different colors to beytter keep track them. 
