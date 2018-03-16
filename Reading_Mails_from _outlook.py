import Outlook

mail = Outlook.Outlook()
mail.login('sampada.itape@mindtree.com','L1nuxc0mm@nds')
mail.inbox()
print mail.unread()