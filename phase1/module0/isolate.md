# Virtual environments
A virtual environment isolates project dependencies. Without one, you'll eventually break your system Python. 

*Make a venv for every project.*

```
# Create one
python3 -m venv venv

# Activate it
source venv/bin/activate         # Mac/Linux
venv\Scripts\activate            # Windows

# When you're done
deactivate
```
