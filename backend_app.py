#!/usr/bin/env python
# coding: utf-8



# In[2]:


from flask import Flask, render_template, request


# In[4]:


app = Flask(__name__)


# In[5]:


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


# In[ ]:


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_prime', methods=['POST'])
def check_prime():
    number = int(request.form['number'])
    if is_prime(number):
        result = f"{number} is a prime number."
    else:
        result = f"{number} is not a prime number."

    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

