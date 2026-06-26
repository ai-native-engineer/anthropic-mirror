<!-- source: https://platform.claude.com/docs/en/managed-agents/files -->

# Adding files
Upload files and mount them in your sandbox for reading and processing.
You can provide files to your agent by uploading them through the Files API and mounting them in the session's sandbox.
All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. The SDK sets the beta header automatically.
Uploading files
First, upload a file using the [Files API](https://platform.claude.com/docs/en/build-with-claude/files):
curlCLIPythonTypeScriptC#GoJavaPHPRuby

file = client.beta.files.upload(file=Path("data.csv"))
print(f"File ID: {file.id}")

Mounting files in a session
Mount uploaded files into the sandbox by adding them to the `resources` array when creating a session:

The `mount_path` is optional, but make sure the uploaded file has a descriptive name so the agent can identify it.
curlCLIPythonTypeScriptC#GoJavaPHPRuby

session = client.beta.sessions.create(
    agent=agent.id,
    environment_id=environment.id,
    resources=[
            "type": "file",
            "file_id": file.id,
            "mount_path": "/workspace/data.csv",
    ],
)

A new `file_id` is created that references the instance of the file in the session. These copies do not count against your [storage limits](https://platform.claude.com/docs/en/build-with-claude/files).
Multiple files
Mount multiple files by adding entries to the `resources` array:
curlCLIPythonTypeScriptC#GoJavaPHPRuby

resources = [
    {"type": "file", "file_id": "file_abc123", "mount_path": "/workspace/data.csv"},
    {"type": "file", "file_id": "file_def456", "mount_path": "/workspace/config.json"},
    {"type": "file", "file_id": "file_ghi789", "mount_path": "/workspace/src/main.py"},
]

A maximum of 100 files is supported per session.
Managing files on a running session
You can add or remove files from a session after creation using the session resources API. Each resource has an `id` returned when it is added (or listed), which you use for deletes.
curlCLIPythonTypeScriptC#GoJavaPHPRuby

resource = client.beta.sessions.resources.add(
    session.id,
    type="file",
    file_id=file.id,
)
print(resource.id)  # "sesrsc_01ABC..."

List all resources on a session with `resources.list`. To remove a file, call `resources.delete` with the resource ID:
curlCLIPythonTypeScriptC#GoJavaPHPRuby

listed = client.beta.sessions.resources.list(session.id)
for entry in listed.data:
    print(entry.id, entry.type)

client.beta.sessions.resources.delete(resource.id, session_id=session.id)

Listing and downloading session files
Use the [Files API](https://platform.claude.com/docs/en/build-with-claude/files) to list files scoped to a session and download them.
curlCLIPythonTypeScriptC#GoJavaPHPRuby

# List files associated with a session
files = client.beta.files.list(
    scope_id="sesn_abc123",
    betas=["managed-agents-2026-04-01"],
)
for f in files:
    print(f.id, f.filename)

# Download a file
content = client.beta.files.download(files.data[0].id)
content.write_to_file("output.txt")

Supported file types
The agent can work with any file type, including:
  * Source code (`.py`, `.js`, `.ts`, `.go`, `.rs`, and others)
  * Data files (`.csv`, `.json`, `.xml`, `.yaml`)
  * Documents (`.txt`, `.md`)
  * Archives (`.zip`, `.tar.gz`) - the agent can extract these using bash
  * Binary files - the agent can process these with appropriate tools

File paths
Files mounted in the sandbox are read-only copies. The agent can read them but cannot modify the original uploaded file. To work with modified versions, the agent writes to new paths within the sandbox.
  * Files are mounted at the exact path you specify
  * Parent directories are created automatically
  * Paths should be absolute (starting with `/`)

  * [Uploading files](https://platform.claude.com/docs/en/managed-agents/files#uploading-files)
  * [Mounting files in a session](https://platform.claude.com/docs/en/managed-agents/files#mounting-files-in-a-session)
  * [Multiple files](https://platform.claude.com/docs/en/managed-agents/files#multiple-files)
  * [Managing files on a running session](https://platform.claude.com/docs/en/managed-agents/files#managing-files-on-a-running-session)
  * [Listing and downloading session files](https://platform.claude.com/docs/en/managed-agents/files#listing-and-downloading-session-files)
  * [Supported file types](https://platform.claude.com/docs/en/managed-agents/files#supported-file-types)
  * [File paths](https://platform.claude.com/docs/en/managed-agents/files#file-paths)

Managed Agents/Manage agent context
# Adding files
Upload files and mount them in your sandbox for reading and processing.
You can provide files to your agent by uploading them through the Files API and mounting them in the session's sandbox.
All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. The SDK sets the beta header automatically.
Uploading files
First, upload a file using the [Files API](https://platform.claude.com/docs/en/build-with-claude/files):
curlCLIPythonTypeScriptC#GoJavaPHPRuby

file = client.beta.files.upload(file=Path("data.csv"))
print(f"File ID: {file.id}")

Mounting files in a session
Mount uploaded files into the sandbox by adding them to the `resources` array when creating a session:

The `mount_path` is optional, but make sure the uploaded file has a descriptive name so the agent can identify it.
curlCLIPythonTypeScriptC#GoJavaPHPRuby

session = client.beta.sessions.create(
    agent=agent.id,
    environment_id=environment.id,
    resources=[
            "type": "file",
            "file_id": file.id,
            "mount_path": "/workspace/data.csv",
    ],
)

A new `file_id` is created that references the instance of the file in the session. These copies do not count against your [storage limits](https://platform.claude.com/docs/en/build-with-claude/files).
Multiple files
Mount multiple files by adding entries to the `resources` array:
curlCLIPythonTypeScriptC#GoJavaPHPRuby

resources = [
    {"type": "file", "file_id": "file_abc123", "mount_path": "/workspace/data.csv"},
    {"type": "file", "file_id": "file_def456", "mount_path": "/workspace/config.json"},
    {"type": "file", "file_id": "file_ghi789", "mount_path": "/workspace/src/main.py"},
]

A maximum of 100 files is supported per session.
Managing files on a running session
You can add or remove files from a session after creation using the session resources API. Each resource has an `id` returned when it is added (or listed), which you use for deletes.
curlCLIPythonTypeScriptC#GoJavaPHPRuby

resource = client.beta.sessions.resources.add(
    session.id,
    type="file",
    file_id=file.id,
)
print(resource.id)  # "sesrsc_01ABC..."

List all resources on a session with `resources.list`. To remove a file, call `resources.delete` with the resource ID:
curlCLIPythonTypeScriptC#GoJavaPHPRuby

listed = client.beta.sessions.resources.list(session.id)
for entry in listed.data:
    print(entry.id, entry.type)

client.beta.sessions.resources.delete(resource.id, session_id=session.id)

Listing and downloading session files
Use the [Files API](https://platform.claude.com/docs/en/build-with-claude/files) to list files scoped to a session and download them.
curlCLIPythonTypeScriptC#GoJavaPHPRuby

# List files associated with a session
files = client.beta.files.list(
    scope_id="sesn_abc123",
    betas=["managed-agents-2026-04-01"],
)
for f in files:
    print(f.id, f.filename)

# Download a file
content = client.beta.files.download(files.data[0].id)
content.write_to_file("output.txt")

Supported file types
The agent can work with any file type, including:
  * Source code (`.py`, `.js`, `.ts`, `.go`, `.rs`, and others)
  * Data files (`.csv`, `.json`, `.xml`, `.yaml`)
  * Documents (`.txt`, `.md`)
  * Archives (`.zip`, `.tar.gz`) - the agent can extract these using bash
  * Binary files - the agent can process these with appropriate tools

File paths
Files mounted in the sandbox are read-only copies. The agent can read them but cannot modify the original uploaded file. To work with modified versions, the agent writes to new paths within the sandbox.
  * Files are mounted at the exact path you specify
  * Parent directories are created automatically
  * Paths should be absolute (starting with `/`)
