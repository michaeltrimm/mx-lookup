from app import app
from flask import Flask, request, render_template, url_for, flash, redirect, jsonify
import dns.resolver

# Helper Function
def request_wants_json():
    types = request.accept_mimetypes.best_match(['application/json'])
    return types == 'application/json' and \
                    request.accept_mimetypes[types] > \
                    request.accept_mimetypes['text/html']

# Root Path
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


# Process Path Only
@app.route('/check', methods=['POST'])
def check():
  domain = request.form['domain']
  if domain is None or domain == '':
    flash(u'Invalid domain provided', 'error')
    return redirect(url_for('index'))
  else:
    # Determine IP Address for Domain
    ips = set()
    for x in dns.resolver.query(domain, 'A'):
      ips.add(x.to_text().upper())

    # Get MX Records
    mx_records = set()
    for x in dns.resolver.query(domain, 'MX'):
      mx_records.add(x.to_text().upper())

    # Sort Records
    sorted_mx = sorted(mx_records, key=lambda x:x[:2], reverse=False)

    # Handle JSON requests differently or render results template
    if request_wants_json():
      return jsonify(domain=domain, ips=[y for y in ips], mx=[x for x in sorted_mx])
    else:
      return render_template('results.html', results=sorted_mx, domain=domain, ips=ips)
