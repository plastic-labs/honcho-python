# Apps

Types:

```python
from honcho.types import App
```

Methods:

- <code title="post /apps">client.apps.<a href="./src/honcho/resources/apps/apps.py">create</a>(\*\*<a href="src/honcho/types/app_create_params.py">params</a>) -> <a href="./src/honcho/types/app.py">App</a></code>
- <code title="put /apps/{app_id}">client.apps.<a href="./src/honcho/resources/apps/apps.py">update</a>(app_id, \*\*<a href="src/honcho/types/app_update_params.py">params</a>) -> <a href="./src/honcho/types/app.py">App</a></code>
- <code title="get /apps/{app_id}">client.apps.<a href="./src/honcho/resources/apps/apps.py">get</a>(app_id) -> <a href="./src/honcho/types/app.py">App</a></code>
- <code title="get /apps/name/{name}">client.apps.<a href="./src/honcho/resources/apps/apps.py">get_by_name</a>(name) -> <a href="./src/honcho/types/app.py">App</a></code>
- <code title="get /apps/get_or_create/{name}">client.apps.<a href="./src/honcho/resources/apps/apps.py">get_or_create</a>(name) -> <a href="./src/honcho/types/app.py">App</a></code>

## Users

Types:

```python
from honcho.types.apps import PageUser, User
```

Methods:

- <code title="post /apps/{app_id}/users">client.apps.users.<a href="./src/honcho/resources/apps/users/users.py">create</a>(app_id, \*\*<a href="src/honcho/types/apps/user_create_params.py">params</a>) -> <a href="./src/honcho/types/apps/user.py">User</a></code>
- <code title="put /apps/{app_id}/users/{user_id}">client.apps.users.<a href="./src/honcho/resources/apps/users/users.py">update</a>(user_id, \*, app_id, \*\*<a href="src/honcho/types/apps/user_update_params.py">params</a>) -> <a href="./src/honcho/types/apps/user.py">User</a></code>
- <code title="get /apps/{app_id}/users">client.apps.users.<a href="./src/honcho/resources/apps/users/users.py">list</a>(app_id, \*\*<a href="src/honcho/types/apps/user_list_params.py">params</a>) -> <a href="./src/honcho/types/apps/user.py">SyncPage[User]</a></code>
- <code title="get /apps/{app_id}/users/{user_id}">client.apps.users.<a href="./src/honcho/resources/apps/users/users.py">get</a>(user_id, \*, app_id) -> <a href="./src/honcho/types/apps/user.py">User</a></code>
- <code title="get /apps/{app_id}/users/name/{name}">client.apps.users.<a href="./src/honcho/resources/apps/users/users.py">get_by_name</a>(name, \*, app_id) -> <a href="./src/honcho/types/apps/user.py">User</a></code>
- <code title="get /apps/{app_id}/users/get_or_create/{name}">client.apps.users.<a href="./src/honcho/resources/apps/users/users.py">get_or_create</a>(name, \*, app_id) -> <a href="./src/honcho/types/apps/user.py">User</a></code>

### Metamessages

Types:

```python
from honcho.types.apps.users import PageMetamessage
```

Methods:

- <code title="get /apps/{app_id}/users/{user_id}/metamessages">client.apps.users.metamessages.<a href="./src/honcho/resources/apps/users/metamessages.py">list</a>(user_id, \*, app_id, \*\*<a href="src/honcho/types/apps/users/metamessage_list_params.py">params</a>) -> <a href="./src/honcho/types/apps/users/sessions/metamessage.py">SyncPage[Metamessage]</a></code>

### Sessions

Types:

```python
from honcho.types.apps.users import AgentChat, PageSession, Session, SessionDeleteResponse
```

Methods:

- <code title="post /apps/{app_id}/users/{user_id}/sessions">client.apps.users.sessions.<a href="./src/honcho/resources/apps/users/sessions/sessions.py">create</a>(user_id, \*, app_id, \*\*<a href="src/honcho/types/apps/users/session_create_params.py">params</a>) -> <a href="./src/honcho/types/apps/users/session.py">Session</a></code>
- <code title="put /apps/{app_id}/users/{user_id}/sessions/{session_id}">client.apps.users.sessions.<a href="./src/honcho/resources/apps/users/sessions/sessions.py">update</a>(session_id, \*, app_id, user_id, \*\*<a href="src/honcho/types/apps/users/session_update_params.py">params</a>) -> <a href="./src/honcho/types/apps/users/session.py">Session</a></code>
- <code title="get /apps/{app_id}/users/{user_id}/sessions">client.apps.users.sessions.<a href="./src/honcho/resources/apps/users/sessions/sessions.py">list</a>(user_id, \*, app_id, \*\*<a href="src/honcho/types/apps/users/session_list_params.py">params</a>) -> <a href="./src/honcho/types/apps/users/session.py">SyncPage[Session]</a></code>
- <code title="delete /apps/{app_id}/users/{user_id}/sessions/{session_id}">client.apps.users.sessions.<a href="./src/honcho/resources/apps/users/sessions/sessions.py">delete</a>(session_id, \*, app_id, user_id) -> <a href="./src/honcho/types/apps/users/session_delete_response.py">object</a></code>
- <code title="get /apps/{app_id}/users/{user_id}/sessions/{session_id}">client.apps.users.sessions.<a href="./src/honcho/resources/apps/users/sessions/sessions.py">get</a>(session_id, \*, app_id, user_id) -> <a href="./src/honcho/types/apps/users/session.py">Session</a></code>

#### Messages

Types:

```python
from honcho.types.apps.users.sessions import Message, PageMessage
```

Methods:

- <code title="post /apps/{app_id}/users/{user_id}/sessions/{session_id}/messages">client.apps.users.sessions.messages.<a href="./src/honcho/resources/apps/users/sessions/messages.py">create</a>(session_id, \*, app_id, user_id, \*\*<a href="src/honcho/types/apps/users/sessions/message_create_params.py">params</a>) -> <a href="./src/honcho/types/apps/users/sessions/message.py">Message</a></code>
- <code title="put /apps/{app_id}/users/{user_id}/sessions/{session_id}/messages/{message_id}">client.apps.users.sessions.messages.<a href="./src/honcho/resources/apps/users/sessions/messages.py">update</a>(message_id, \*, app_id, user_id, session_id, \*\*<a href="src/honcho/types/apps/users/sessions/message_update_params.py">params</a>) -> <a href="./src/honcho/types/apps/users/sessions/message.py">Message</a></code>
- <code title="get /apps/{app_id}/users/{user_id}/sessions/{session_id}/messages">client.apps.users.sessions.messages.<a href="./src/honcho/resources/apps/users/sessions/messages.py">list</a>(session_id, \*, app_id, user_id, \*\*<a href="src/honcho/types/apps/users/sessions/message_list_params.py">params</a>) -> <a href="./src/honcho/types/apps/users/sessions/message.py">SyncPage[Message]</a></code>
- <code title="get /apps/{app_id}/users/{user_id}/sessions/{session_id}/messages/{message_id}">client.apps.users.sessions.messages.<a href="./src/honcho/resources/apps/users/sessions/messages.py">get</a>(message_id, \*, app_id, user_id, session_id) -> <a href="./src/honcho/types/apps/users/sessions/message.py">Message</a></code>

#### Metamessages

Types:

```python
from honcho.types.apps.users.sessions import Metamessage, PageMetamessage
```

Methods:

- <code title="post /apps/{app_id}/users/{user_id}/sessions/{session_id}/metamessages">client.apps.users.sessions.metamessages.<a href="./src/honcho/resources/apps/users/sessions/metamessages.py">create</a>(session_id, \*, app_id, user_id, \*\*<a href="src/honcho/types/apps/users/sessions/metamessage_create_params.py">params</a>) -> <a href="./src/honcho/types/apps/users/sessions/metamessage.py">Metamessage</a></code>
- <code title="put /apps/{app_id}/users/{user_id}/sessions/{session_id}/metamessages/{metamessage_id}">client.apps.users.sessions.metamessages.<a href="./src/honcho/resources/apps/users/sessions/metamessages.py">update</a>(metamessage_id, \*, app_id, user_id, session_id, \*\*<a href="src/honcho/types/apps/users/sessions/metamessage_update_params.py">params</a>) -> <a href="./src/honcho/types/apps/users/sessions/metamessage.py">Metamessage</a></code>
- <code title="get /apps/{app_id}/users/{user_id}/sessions/{session_id}/metamessages">client.apps.users.sessions.metamessages.<a href="./src/honcho/resources/apps/users/sessions/metamessages.py">list</a>(session_id, \*, app_id, user_id, \*\*<a href="src/honcho/types/apps/users/sessions/metamessage_list_params.py">params</a>) -> <a href="./src/honcho/types/apps/users/sessions/metamessage.py">SyncPage[Metamessage]</a></code>
- <code title="get /apps/{app_id}/users/{user_id}/sessions/{session_id}/metamessages/{metamessage_id}">client.apps.users.sessions.metamessages.<a href="./src/honcho/resources/apps/users/sessions/metamessages.py">get</a>(metamessage_id, \*, app_id, user_id, session_id, \*\*<a href="src/honcho/types/apps/users/sessions/metamessage_get_params.py">params</a>) -> <a href="./src/honcho/types/apps/users/sessions/metamessage.py">Metamessage</a></code>

### Collections

Types:

```python
from honcho.types.apps.users import Collection, PageCollection, CollectionDeleteResponse
```

Methods:

- <code title="post /apps/{app_id}/users/{user_id}/collections">client.apps.users.collections.<a href="./src/honcho/resources/apps/users/collections/collections.py">create</a>(user_id, \*, app_id, \*\*<a href="src/honcho/types/apps/users/collection_create_params.py">params</a>) -> <a href="./src/honcho/types/apps/users/collection.py">Collection</a></code>
- <code title="put /apps/{app_id}/users/{user_id}/collections/{collection_id}">client.apps.users.collections.<a href="./src/honcho/resources/apps/users/collections/collections.py">update</a>(collection_id, \*, app_id, user_id, \*\*<a href="src/honcho/types/apps/users/collection_update_params.py">params</a>) -> <a href="./src/honcho/types/apps/users/collection.py">Collection</a></code>
- <code title="get /apps/{app_id}/users/{user_id}/collections">client.apps.users.collections.<a href="./src/honcho/resources/apps/users/collections/collections.py">list</a>(user_id, \*, app_id, \*\*<a href="src/honcho/types/apps/users/collection_list_params.py">params</a>) -> <a href="./src/honcho/types/apps/users/collection.py">SyncPage[Collection]</a></code>
- <code title="delete /apps/{app_id}/users/{user_id}/collections/{collection_id}">client.apps.users.collections.<a href="./src/honcho/resources/apps/users/collections/collections.py">delete</a>(collection_id, \*, app_id, user_id) -> <a href="./src/honcho/types/apps/users/collection_delete_response.py">object</a></code>
- <code title="get /apps/{app_id}/users/{user_id}/collections/{collection_id}">client.apps.users.collections.<a href="./src/honcho/resources/apps/users/collections/collections.py">get</a>(collection_id, \*, app_id, user_id) -> <a href="./src/honcho/types/apps/users/collection.py">Collection</a></code>
- <code title="get /apps/{app_id}/users/{user_id}/collections/name/{name}">client.apps.users.collections.<a href="./src/honcho/resources/apps/users/collections/collections.py">get_by_name</a>(name, \*, app_id, user_id) -> <a href="./src/honcho/types/apps/users/collection.py">Collection</a></code>

#### Documents

Types:

```python
from honcho.types.apps.users.collections import Document, PageDocument, DocumentDeleteResponse
```

Methods:

- <code title="post /apps/{app_id}/users/{user_id}/collections/{collection_id}/documents">client.apps.users.collections.documents.<a href="./src/honcho/resources/apps/users/collections/documents.py">create</a>(collection_id, \*, app_id, user_id, \*\*<a href="src/honcho/types/apps/users/collections/document_create_params.py">params</a>) -> <a href="./src/honcho/types/apps/users/collections/document.py">Document</a></code>
- <code title="put /apps/{app_id}/users/{user_id}/collections/{collection_id}/documents/{document_id}">client.apps.users.collections.documents.<a href="./src/honcho/resources/apps/users/collections/documents.py">update</a>(document_id, \*, app_id, user_id, collection_id, \*\*<a href="src/honcho/types/apps/users/collections/document_update_params.py">params</a>) -> <a href="./src/honcho/types/apps/users/collections/document.py">Document</a></code>
- <code title="get /apps/{app_id}/users/{user_id}/collections/{collection_id}/documents">client.apps.users.collections.documents.<a href="./src/honcho/resources/apps/users/collections/documents.py">list</a>(collection_id, \*, app_id, user_id, \*\*<a href="src/honcho/types/apps/users/collections/document_list_params.py">params</a>) -> <a href="./src/honcho/types/apps/users/collections/document.py">SyncPage[Document]</a></code>
- <code title="delete /apps/{app_id}/users/{user_id}/collections/{collection_id}/documents/{document_id}">client.apps.users.collections.documents.<a href="./src/honcho/resources/apps/users/collections/documents.py">delete</a>(document_id, \*, app_id, user_id, collection_id) -> <a href="./src/honcho/types/apps/users/collections/document_delete_response.py">object</a></code>
- <code title="get /apps/{app_id}/users/{user_id}/collections/{collection_id}/documents/{document_id}">client.apps.users.collections.documents.<a href="./src/honcho/resources/apps/users/collections/documents.py">get</a>(document_id, \*, app_id, user_id, collection_id) -> <a href="./src/honcho/types/apps/users/collections/document.py">Document</a></code>
