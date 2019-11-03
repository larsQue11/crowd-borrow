import connect_to_firebase
import get_accounts_ncr

connection_firestore = connect_to_firebase.get_firestore_connection()
users_collection = connection_firestore.collection('crowd_borrow_accounts')
recipients_ncr = get_accounts_ncr.get_account_ncr()

users_collection.document(recipients_ncr["accountNumber"]).set(recipients_ncr)