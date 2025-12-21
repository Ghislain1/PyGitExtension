from PyQt6.QtCore import QObject

from models.counter_model import CounterModel
from models.user_model import User
from services.user_serivce import UserService
from viewmodels.count_vm import CounterViewModel
from viewmodels.user_vm import UserViewModel


# viewmodels/main_vm.py
class MainViewModel(QObject):
    """MainViewModel as a composition root for all other ViewModels."""

    def __init__(self):
        super().__init__()

        # Create a user model & ViewModel HERE
        user_model = User(name="Alice", email="alice@example.com")
        self.user_vm = UserViewModel(user_model, UserService)  # No service for now

        # Counter
        counter_model = CounterModel()
        self.counter_vm = CounterViewModel(counter_model)

        # self.product_vm = ProductViewModel(...)
        # self.order_vm = OrderViewModel(...)
        # self.invoice_vm = InvoiceViewModel(...)
        # self.settings_vm = SettingsViewModel(...)
