# generate_html.py
#!/usr/bin/python
html_content = """
# Mencetak konten ke konsol (opsional)
print("--- Konten HTML yang Dihasilkan ---")
print("html_content")

# Menyimpan konten ke file HTML
with open("login.html.py", "w") as f:
    f.write(html_content)

print("--- File index.html berhasil dibuat ---")

<!DOCTYPE html>
print("Silahkan login untuk mulai bermain")
                        <div>
                            <input type="hidden" id="ceklogin" value="/json/post/ceklogin">
                            <!-- login form and button -->
                            <div class="login-wrapper">
                                <form onsubmit="md5nohash(entered_password, vb_login_md5password, vb_login_md5password_utf, 0)">
                                    <div class="form-input">
                                        <div class="form-group">
                                            <input id="navbar_username" name="entered_login" tabindex="1" class="contactField requiredField center" type="text" value="" placeholder="Username" onblur="if(this.value == '') { this.value='Username'}" onfocus="if (this.value == 'Username') {this.value=''}" required="">
                                        </div>
                                        <div class="form-group password-wrapper">
                                            <input id="navbar_password" type="password" tabindex="2" name="entered_password" class="contactField requiredField center" value="" placeholder="Password" onblur="if(this.value == '') { this.value='Password'}" onfocus="if (this.value == 'Password') {this.value=''}" required="">
                                            <button type="button" onclick="showPass()">
                                                <svg id="show-pass-icon" class="active" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path>
                                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path>
                                                </svg>
                                            </button>
                                        </div>
                                    </div>
                                    <div>
                                        <a href="/lite" class="note left">Versi WAP (KLIK DISINI)</a>
                                                                                    <a href="/forgot/password" class="note right underline">Lupa password?</a>
                                        
                                        <div class="buttonjoin">
                                            <input type="submit" name="Submit" class="buttonWrap buttons button-blue contactSubmitButton" value="Log in" id="loginBtnHeader">
                                        </div>
                                    </div>
                                </form>
