# Virtual environments
A virtual environment isolates project dependencies. Without it, you'll eventually break your system Python. 

*Make a venv for every project.*

```
# Create one
uv venv

# Activate it
source venv/bin/activate         # Mac/Linux
venv\Scripts\activate            # Windows

# When you're done
deactivate
```
