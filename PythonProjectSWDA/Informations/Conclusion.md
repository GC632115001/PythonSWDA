# Conclusion


##  Problem 1) Incorrect trust assumptions (S01)
    Solution 1.) Make sure all data from an untrusted client are validated(S01)
##  Drivers
* approachability (S01)
* chosen tools (S01)


##  Problem 2) SQL Injection (S19, S29, S36)
	Solution 1.) Using parameterized queries instead of dynamic SQL statements. (S19)
    Solution 2.) Using a web application firewall (WAF) (S29)
	Solution 3.) Don’t use dynamic SQL (S36)
##  Drivers
* code language (S19, S29, S36)
* approachability, (S19, S29) 
* chosen tools (S19)


##  Problem 3) an unauthorized entity having access to a system or service that it should not (S01, S02, S10 )
    Solution 1.) Implement Principle of Least Privilege (S01)
	Solution 2.) Train employees on cyber security best practices (S02)
	Solution 3.) Architecture analysis assessments (S10)
##  Drivers
* approachability (S01 , S10)
* chosen tools (S01)
* team cohesion (S02)
* code language (S02)


##  Problem 4) Neglecting to authorize after authentication (S01, S04, S18, S24, S26, S27)
    Solution 1.) Periodically perform authorization as an explicit check (S01)
	Solution 2.) Adopt automated testing (S04)
	Solution 3.) Implement strong authentication methods such as multi-factor authentication (MFA) to reduce the risk of unauthorized access.(S18)
	Solution 4.) Implementing a framework will help you avoid the web security risks caused by faulty authentication. (S24)
	Solution 5.) Use OAuth2 for single sign on (SSO) with OpenID Connect. (S26)
	Solution 6.) Add more Authentication ex. Multi-factor authentication, Certificate-based authentication, Biometric authentication, and Token-based authentication.(S27)
## Drivers
* approachability (S01, S18)
* chosen tools (S01)
* team cohesion (S04, S18)
* stakeholders (S04)
* code language (S04,S18)
* time consuming (S18)


## Problem 5) Data breaches(S02, S40)
    Solution 1.) Use secure coding practices (S02, S40)
## Drivers
* team cohesion (S02)
* code langugae (S40)


## Problem 6) Poor key management  (S01, S05)
    Solution 1.) Strict policy-based controls to prevent the misuse/reuse of keys (S01)
	Solution 2.) Secure coding guidelines and standards (S05)
## Drivers
* approachability(S01)
* chosen tools (S01)
* code language (S05)


## Problem 7) Failure to centralize cryptography (S01, S09)
	Solution 1.) Use Updated and Established Cryptographic Functions, Algorithms, and Protocols (S01)
	Solution 2.) Blockchain-powered cybersecurity controls and standards to defend enterprises against cyberattacks. (S09)
## Drivers
* approachability (S01, S09)
* chosen tools (S01)


## Problem 8) Malware(S02, S31, S32, S40)
    Solution 1.) Monitor systems for cyber threats (S02, S40)
	Solution 2.) Change your passwords frequently. (S31)
	Solution 3.) Enable and require multi factor authentication (MFA) , OTP ,2FA (S32)
## Drivers
* code language (S02)
* team cohesion (S02)
* approachability (S40)
* chosen tools (S40, S31, S32)


## Problem 9) Insecure APIs (S03, S04, S12, S22, S37, S39, S40)
    Solution 1.) Establishing a policy on open-source use (S03)
    Solution 2.) Scan for vulnerabilities regularly (S04)
    Solution 3.) Code review involves reviewing the code written by developers to identify potential security issues (S12)
    Solution 4.) Reducing misconfigurations and monitoring for security issues (S22)
	Solution 5.) Use the services that focus on checking codebase dependencies (S37)
	Solution 6.) Integrating a scanning tool like Software Composition Analysis (SCA) (S39)
	Solution 7.) Implement multi-factor authentication (S40)
## Drivers
* team cohesion (S03, S04)
* code language (S03)
* chosen tools (S03)


## Problem 10) Poor passwords, Weak passwords, and password reuse (S02,S19,S30,S32,S34)
    Solution 1.) Use security testing (S02)
	Solution 2.) Use a password hashing technique to generate a unique hash of the user's password that could be saved in database (S19)
    Solution 3.) Using a strong passwords that difficult to crack, ex. At least seven characters long, Contains "secret" or random information, Is significantly different from previous passwords, Uppercase letters, Lowercase letters, Numerals, and Symbols including spaces (S30)
    Solution 4.) Maintain good password hygiene (S32)
    Solution 5.) Weakened Security Measures (S34)
## Drivers
* team cohesion (S02) 
* code language (S02, S19)
* approachability (S19)
* chosen tools (S19)
* enhance security (S30)


## Problem 11) Inadequate Security Awareness and Training (S03, S07, S13, S14, S17, S20, S21, S22, S23, S37)
	Solution 1.) dedicated time to focus on security awareness education and security protocol training(S03, S07, S21, S22) 
    Solution 2.) Seek advice from security experts to identify security challenges effectively.(S13)
    Solution 3.) Collaborating in an agile, sprint-based model to defend against cyberattacks.(S14)
	Solution 4.) Organizations should foster a culture that emphasizes the importance of software security(S17)
	Solution 6.)Shift Left and Adopt DevSecOps(S20)
	Solution 7.) Strive to achieve agile security. Use modern software supply chain security tools like Legit Security that provides an aggregated security score by product line and development team(S23)
	Solution 8.) Consider which items are most applicable to your organization, and then start making necessary adjustments.(S37)
## Drivers
* team cohesion (S03, S14, S17, S20, S23, S37)
* code language (S03, S20, S37)
* chosen tools (S03, S21, S22, S37)
* prioritization (S13, S17, S20, S21)
* workforce crisis (S07)
* approachability (S13, S14, S21, S23)
* stakeholders (S13, S14, S17, S37)
* increasingly complex cyberattacks (S07)
* knowledge and experience.(S17)
* time consuming (S20, S22, S37)


## Problem 12) Failing to Prioritize the Security Team (S03, S08, S13, S17, S21, S23)
    Solution 1.) drive a cultural change that makes secure development a non-negotiable priority (S03)
    Solution 2.) Better collaboration and cautious coding from all parties involved. (S08)
    Solution 3.) Require ongoing security training for the development team, and require that all newly developed APIs, microservices, integrations, and applications instrument the required security tests in their CI/CD pipelines. (S13)
    Solution 4.) Prioritize security and recognize it as an essential aspect of software development (S17)
	Solution 5.) Take the time to learns about security (S21)
	Solution 6.) Spend time re-framing security procedures so that team members understand why a certain security practice is important (S23)
## Drivers
* team cohesion (S03, S13, S17, S23)
* code language (S03)
* chosen tools (S03, S21)
* Company structure for only speed and profit (S08)
* Prioritization (S13, S17, S21)
* stakeholders (S13, S17)
* approachability (S13, S21, S23)
* knowledge and experience. (S17)


## Problem 13) Weak backend access controls (S04, S06, S24)
    Solution 1.) Scan for vulnerabilities regularly (S04)
    Solution 2.) Restricted user to only necessary area (S06)
    Solution 3.) Restrict access and use a password once saved (S24)
## Drivers
* team cohesion (S04)
* code language (S04, S06)
* stakeholders (S04, S06)
* implementation technology (S06)
* approachability (S24)


## Problem 14) Poorly written code(S05,S18,S20,S37)
    Solution 1.) Treat Software Security as a Priority Right From The Start (S05)
    Solution 2.) Conduct testing to identify and address coding bugs. Implement secure coding practices and perform regular code reviews to minimize the introduction of vulnerabilities (S18)
    Solution 3.) Maintain an OSS Security Library Inventory (S20)
    Solution 4.) Verify that the code is efficient, scalable and secure (S37)
## Drivers
* team cohesion (S05, S18, S20, S37)
* code language (S05, S18, S20, S37)
* Implementation methodology (S18)
* time consuming (S18, S20)
* prioritization (S20)
* chosen tools (S37)
* stakeholders(S37)


## Problem 15) Security misconfiguration (S04)
    Solution 1.) Include application security in data privacy compliance strategy (S04)
## Drivers
* code language (S04)
* implementation methodology (S04)
* frameworks and libraries (S04)
* team cohesion (S04)


## Problem 16) Insufficient Logging & Monitoring(S03, S04, S12, S19, S40)
    Solution 1.) dedicated time to focus on security awareness education and security protocol training (S03)
    Solution 2.) Implement Principle of Least Privilege (S04)
    Solution 3.) Continuous monitoring helps in detecting and responding to security incidents in real-time (S12)
    Solution 4.) User activity tracking, file integrity monitoring, and network activity logs are examples of monitoring and auditing practices (S19)
	Solution 5.) Use security testing (S40)
## Drivers
* team cohesion (S03, S04)
* code language (S03, S04, S19)
* chosen tools (S03, S19, S40)
* stakeholders (S04)
* approachability (S19, S40)


## Problem 17) Unfettered access to source code repositories and CI/CD pipelines(S13, S23, S38)
    Solution1.) Implement automated security testing, avoid access to repositories, and apply the principle of least privilege.(S13)
    Solution2.) Set limitations or privacy to access source code(S23)
    Solution3.) Use static analytical methods to design and test components.(S38)


## Drivers
* Prioritization (S13)
* Stakeholders(including third-party) (S13)
* Approachability (S13, S23)
* Team cohesion (decision-making) (S13, S23, S38)
* Chosen tools (S38)


## Problem 18) Exposure of sensitive data(S06,S11,S13,S42)
	Solution1.) Personal or sensitive data has to be protected with encryption  (S06)
    Solution2.) Adopt data governance, educate on data practices, centralized identity management, and implement data lineage capabilities. (S11, S13)
    Solution3.) Eliciting requirements carefully, including security requirements(S42)
## Drivers
* Prioritization (S13, S42)
* Stakeholders (S06, S13)
* approachability (S13)
* Team cohesion (decision-making) (S13)
* Implementation technology (S06)
* Code language (S06)
* Negligent (S11)
* Chosen tools (S42)
* Team decision-making (S42)


## Problem 19) Legacy software (S05)
	Solution1.) Make sure to use software that is updated regularly  (S05)
## Drivers
* Code language (S05)
* Team cohesion (decision-making) (S05)


## Problem 20) Ransomware Attacks (S07)
	Solution1.) Prioritize cybersecurity more in budgeting  (S07)
## Drivers
* Workforce crisis (S07) 
* Increasingly complex cyberattacks (S07)


## Problem 21) Insufficient collaboration between each member of the company (S08)
	Solution1.) Better collaboration and cautious coding from all parties involved  (S08)
## Drivers
* Company structure (S08) 


## Problem 22) Session Hijacking Attack (S15, S18, S28, S31)
	Solution1.)  Encrypt session data, use strong and unpredictable session IDs, regularly regenerate session IDs, securely store session files, set session timeouts, implement strong user authentication, and keep software updated (S15, S28)
	Solution2.) Implement session management mechanisms, such as setting expiration time for sessions after a period of inactivity. (S18)


## Drivers
* Code language (S15, S18, S28)
* Implementation methodology (S15)
* Fameworks and libraries (S15, S28)
* Team decision-making. (S15)
* Implementation methodology (S18)
* Chosen tools (S28)
* Team cohesion (decision-making) (S28)


## Problem 23) Fault is irrelevant (S08, S42)
	Solution1.) Security teams should focus on vulnerabilities by evaluating their scope, managing the risks (S87)
	Solution2.)  Running automatic test cases to detect difficult risks (S42)
## Drivers
* Company structure (S08) 
* Team decision-making (S42)
* Chosen tools (S42)
* Prioritization (S42)




## Problem 24) Vague requirements (S08)
	Solution1.) Introduce specific requirements focused on incremental steps to improving security  (S08)
## Drivers 
- Company structure (S08) 




## Problem 25) Adapting To A Remote Workforce (S09)
    Solution1.) Implement cloud-based cybersecurity solutions that protect the user's identity, device, and the cloud (S09)
## Drivers
* Lack of updates regarding security (S09)


## Problem 26) Phishing And Spear-Phishing Attacks (S09)
	Solution1.) Use anti-phishing tools such as Antivirus software and Anti-phishing Toolbar, sandbox the E-mail attachments, and train the employees. (S09)
## Drivers
* Lack of updates regarding security (S09)


## Problem 27) Point-of-sale (POS) intrusions (S10)
    Solution1.) Architecture analysis assessments (S10)
## Drivers
* Lack of security controls, inadequate system design (S10)


## Problem 28) Encryption Weakness (S11, S19)
    Solution1.) Plan better protection like encrypting data on USB sticks, laptops, and desktops. (S11)
    Solution2.) All data should be encrypted in transit and at rest.  This includes database storage, file storage, sessions, cookies, etc. (S19)
## Drivers
* Negligent (S11)
* Code language, approachability, chosen tools (S19)


## Problem 29) Insufficient transport layer protection (S11)
    Solution1.) Secure the data transportation (S11)
## Drivers
* Negligent (S11)


## Problem 30) Cross-site scripting (XSS) (S12, S40)
    Solution1.) Developers must adhere to secure coding practices (S12)
    Solution2.) Monitor systems for cyber threats (S40)
## Drivers
* Secure Software Isn’t a Big Enough Priority, Quality Doesn’t Necessarily Guarantee Security, Not Enough Training for Security (S12)
* Approachability, chosen tools (S40)


## Problem 31) Frustrations due to inadequate tooling (S21)
    Solution1.) Avoid depending on SAST tools, as it's vulnerable to triggering several false warnings. (S21)
## Drivers
* Approachability, chosen tools, prioritization (S21)


## Problem 32) Man-in-the-middle (MitM) attacks (S32)
    Solution1.) Properly scope permissions across users and machines (S32)
## Drivers
* N/A


## Problem 33) Brute-force attacks (S33)
    Solution1.) Locking the account that the remote user is trying to access if they make too many failed login attempts . Blocking the remote user's IP address if they make too many login attempts in quick succession (S33)
## Drivers
* N/A


## Problem 34) Have ineffective Software Development Life Cycle. (S17, S23, S37)
    Solution1.) Incorporate security practices and requirements into Agile processes. (S17)
    Solution2.) Focus on ensuring that security vulnerability testing protocols are followed. (S23)
    Solution3.) Do threat modeling during your application planning. (S37)
## Drivers
* code language (S37)
* chosen tools (S37)
* stakeholders (S17, S37)
* approachability (S37)
* team cohesion (decision making) (S17, S23, S27)
* Prioritization (S17)
* Knowledge and experience (S17)




## Problem 35) Unsanitized Input (S36)
    Solution 1.) Avoid placing user-provided input directly into SQL statements(S36)
## Drivers
* N/A


## Problem 36) Cross-Site Request Forgery (CSRF) (S24)
    Solution 1.) Add a secret token in a form field that is hidden and inaccessible to software.(S24)
## Drivers
* Approachability (S24)


## Problem 37) Malicious attacks (S41)
    Solution 1.) Use Software Security Tools(S41)
	Solution 2.) Ensuring and Improving Software Security(S41)
## Drivers
* Approachability (S41)
* chosen tools (S41)


## Problem 38) Unpatched vulnerabilities (S25, S40)
	Solution 1.) Change to HTTPS, That provides protection against these vulnerabilities by encrypting all exchanges between a web browser and web server. As a result, HTTPS ensures that no one can tamper with these transactions, thus securing users' privacy and preventing sensitive information from falling into the wrong hands.(S25)
    Solution 2.) Train employees on cyber security best practices(S40)
## Drivers
* Enhance security (S25)
* approachability (S40)
* chosen tools (S40)


## Problem 39) Lack of defense in depth (S18)
	Solution 1.) Implement multiple layers of security defenses to reduce the likelihood of a successful attack. (S18)
## Drivers
* Code language (S18)
* Implementation methodology  (S18)
* team decision-making (S18)
*  time consuming (S18)


## Problem 40) Fragmented tools and one-off solutions (S16)
	Solution 1.) Adopt a comprehensive security architecture approach for enterprise risk management, avoiding on disconnected tools. (S16)
##  Drivers
* Chosen tools (S16)
*  team cohesion (decision making) (S16)
*  stakeholders (S16)
* implementation methodology or technique.(S16)


##  Problem 41) Lack of comprehensive architectural framework for IT security (S16, S42)
	Solution 1.) Develop an overall security architecture blueprint to optimize resource placement and support business functions. (S16)
    Solution 2.) Educating the development team on security SDLC (S42)
##  Drivers
* Chosen tools (S16, S42)
* team cohesion (decision making) (S16, S42)
* stakeholders (S16, S42)
* implementation methodology or technique. (S16, S42)


##  Problem 42) Insufficient hardware and software security measures. (S16)
    Solution 1.) Implement robust security measures. For example firewalls, encryption. (S16)
##  Drivers
* Chosen tools (16)
* team cohesion (decision making) (16)
* stakeholders (16)
* implementation methodology (16)