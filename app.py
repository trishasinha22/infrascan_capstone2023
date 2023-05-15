from flask import Flask, render_template, request
import SQL_file
import XSS_file
import url_redirect
import csrf_file

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template('home.html')

@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
        # Get the form input values
        url1 = request.form
        result = SQL_file.scan_for_sql_injection_vulnerabilities(url1)
        output = XSS_file.xss_scan(url1)
        output1 = url_redirect.check_url(url1)
        output2 = csrf_file.csrf_scanner(url1)


        #result = SQL_file.scan_for_sql(url1)
       # result =  SQL_file.result_out(url1)
        # Call a Python function with the form inputs
        # Render a template with the result
        #return render_template('result.html',output1=output1)

        return render_template('result.html', result=result, output=output,output1=output1,output2=output2)

    # Render the form template for GET requests
   
if __name__ == '__main__':
    app.run(debug=True)
