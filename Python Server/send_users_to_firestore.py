import connect_to_firebase
import get_recipients_ncr

connection_firestore = connect_to_firebase.get_firestore_connection()
users_collection = connection_firestore.collection('crowd_borrow_users')
recipients_ncr = get_recipients_ncr.get_all_recipients_ncr()

for data in recipients_ncr:
    users_collection.document(data["nickName"]).set(data)
