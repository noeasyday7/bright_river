# parameters.py

param_spaces = {
    "SARIMA": {
        'p': range(1, 3),
        'd': range(0, 2),
        'q': range(1, 3),
        'P': range(0, 2),
        'D': range(0, 2),
        'Q': range(0, 2),
        's': [12]
    },
    "ARIMA": {
        'p': range(1, 3),
        'd': range(0, 2),
        'q': range(1, 3)
    },
    "Exponential Smoothing": {
        'seasonal': ['add', 'mul'],
        'seasonal_periods': [12]
    },
    "Holt": {
        'exponential': [True, False]
    },
    "XGBRegressor": {
        'n_estimators': range(50, 150),
        'max_depth': range(3, 10),
        'learning_rate': [0.01, 0.1, 0.2]
    },
    "RandomForestRegressor": {
        'n_estimators': [50, 100, 150, 350],
        'max_depth': range(3, 10)
    },
    "LSTM": {
        'units': [50, 100],
        'epochs': [10, 20]
    }
}


optimizer_configs = {
    "SARIMA": {'initial_random': 10, 'num_iteration': 15},
    "ARIMA": {'initial_random': 10, 'num_iteration': 15},
    "XGBRegressor": {'initial_random': 10, 'num_iteration': 10},
    "RandomForestRegressor": {'initial_random': 10, 'num_iteration': 10},
    "LSTM": {'initial_random': 5, 'num_iteration': 10}
}
