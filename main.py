import ynab

import secrets

configuration = ynab.Configuration(
    access_token=secrets.ACCESS_TOKEN
)


class YNABClient:
    def __init__(self, access_token=None):
        """Initialize YNAB API Client."""
        self.configuration = ynab.Configuration(
            access_token=secrets.ACCESS_TOKEN
        )

    def get_budgets(self):
        """Fetch the List of Budgets."""
        with ynab.ApiClient(self.configuration) as api_client:
            budgets_api = ynab.BudgetsApi(api_client)
            try:
                budgets_response = budgets_api.get_budgets()
                return budgets_response.data.budgets
            except Exception as e:
                print(f"Error fetching budgets: {e}")
                return []

    def get_transactions(self, budget_id):
        """Fetch transactions for a given budget ID"""
        with ynab.ApiClient(configuration) as api_client:
            transactions_api = ynab.TransactionsApi(api_client)
            try:
                transact_response = transactions_api.get_transactions(budget_id)
                return transact_response.data.transactions
            except Exception as e:
                print('Exception when calling TransactionsApi->get_transactions: %s\n' % e)
                return []

    def get_accounts(self, budget_id):
        """Fetch accounts for a given budegt ID."""
        with ynab.ApiClient(self.configuration) as api_client:
            accounts_api = ynab.AccountsApi(api_client)
            try:
                account_response = accounts_api.get_accounts(budget_id)
                return account_response.data.accounts  # List account objects
            except Exception as e:
                print(f"Error fetching accounts: {e}")
                return []


if __name__ == "__main__":
    ynab_client = YNABClient()

    # Get all budgets
    budgets = ynab_client.get_budgets()
    for budget in budgets:
        print(f"Budget: {budget.name}")
    # Fetch transactions for a specific budget by name
    budget_id = secrets.BANANA_STAND_ID
    if budget_id:
        transactions = ynab_client.get_transactions(budget_id)
        for transaction in transactions[:5]:  # Limit output for now
            print(f"Transaction: {transaction}")

    # Fetch accounts for thr budget
    if budget_id:
        accounts = ynab_client.get_accounts(budget_id)
        for account in accounts:
            print(f"Account: {account.name} (Balance: {account.balance})")
