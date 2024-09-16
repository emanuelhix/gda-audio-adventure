# GDA Audio Adventure

## Purpose
This web application was developed as a GDA icebreaker demo in Fall 2024 by Parker Emanuel Hix (also known as Psudar).

## Recreating the Virtual Environment

To recreate the virtual environment, use the command:

```bash
pip freeze > requirements.txt
```

This will generate a `requirements.txt` file listing all the required modules.
**A `requirements.txt` file should be in the repository home directory already.**

### Activating the Virtual Environment

To activate the virtual environment, run the following command in PowerShell:

```bash
.\venv\Scripts\Activate
```

If you're using PowerShell and encounter an execution policy restriction, you may need to adjust the policy to allow script execution. This step is necessary only if you encounter issues; it is not a security risk. Execution policies are designed to prevent accidental script execution but are easy to modify.

To set the execution policy to unrestricted for the current user, use:

```bash
Set-ExecutionPolicy Unrestricted -Scope CurrentUser
```

For other command prompts, such adjustments are typically not required.