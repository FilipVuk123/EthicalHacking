https://tryhackme.com/room/burpsuitebasics



# What is Burp Suite

In essence, Burp Suite is a Java-based framework designed to serve as a comprehensive solution for conducting web application penetration testing. It has become the industry standard tool for hands-on security assessments of web and mobile applications, including those that rely on application programming interfaces (APIs).

Simply put, Burp Suite captures and enables manipulation of all the HTTP/HTTPS traffic between a browser and a web server. This fundamental capability forms the backbone of the framework. By intercepting requests, users have the flexibility to route them to various components within the Burp Suite framework, which we will explore in upcoming sections. The ability to intercept, view, and modify web requests before they reach the target server or even manipulate responses before they are received by our browser makes Burp Suite an invaluable tool for manual web application testing.





# Features of Burp Community


Although Burp Suite Community offers a more limited feature set compared to the Professional edition, it still provides an impressive array of tools that are highly valuable for web application testing. Let's explore some of the key features:

1. Proxy: The Burp Proxy is the most renowned aspect of Burp Suite. It enables interception and modification of requests and responses while interacting with web applications.
2. Repeater: Another well-known feature. Repeater allows for capturing, modifying, and resending the same request multiple times. This functionality is particularly useful when crafting payloads through trial and error (e.g., in SQLi - Structured Query Language Injection) or testing the functionality of an endpoint for vulnerabilities.
3. Intruder: Despite rate limitations in Burp Suite Community, Intruder allows for spraying endpoints with requests. It is commonly utilized for brute-force attacks or fuzzing endpoints.
4. Decoder: Decoder offers a valuable service for data transformation. It can decode captured information or encode payloads before sending them to the target. While alternative services exist for this purpose, leveraging Decoder within Burp Suite can be highly efficient.
5. Comparer: As the name suggests, Comparer enables the comparison of two pieces of data at either the word or byte level. While not exclusive to Burp Suite, the ability to send potentially large data segments directly to a comparison tool with a single keyboard shortcut significantly accelerates the process.
6. Sequencer: Sequencer is typically employed when assessing the randomness of tokens, such as session cookie values or other supposedly randomly generated data. If the algorithm used for generating these values lacks secure randomness, it can expose avenues for devastating attacks.

# Installation




# The Dashboard




# Navigation

Here's how the navigation works:

- Module Selection: The top row of the menu bar displays the available modules in Burp Suite. You can click on each module to switch between them. For example, the Burp Proxy module is selected in the image below.

- Sub-Tabs: If a selected module has multiple sub-tabs, they can be accessed through the second menu bar that appears directly below the main menu bar. These sub-tabs often contain module-specific settings and options. For example, in the image above, the Proxy Intercept sub-tab is selected within the Burp Proxy module.

- Detaching Tabs: If you prefer to view multiple tabs separately, you can detach them into separate windows. To do this, go to the Window option in the application menu above the Module Selection bar. From there, choose the "Detach" option, and the selected tab will open in a separate window. The detached tabs can be reattached using the same method.


- Ctrl + Shift + D	Dashboard
- Ctrl + Shift + T	Target tab
- Ctrl + Shift + P	Proxy tab
- Ctrl + Shift + I	Intruder tab
- Ctrl + Shift + R	Repeater tab

# Options




# Introduction to the Burp Proxy


## Key Points to Understand About the Burp Proxy
Intercepting Requests: When requests are made through the Burp Proxy, they are intercepted and held back from reaching the target server. The requests appear in the Proxy tab, allowing for further actions such as forwarding, dropping, editing, or sending them to other Burp modules. To disable the intercept and allow requests to pass through the proxy without interruption, click the Intercept is on button.



- Taking Control: The ability to intercept requests empowers testers to gain complete control over web traffic, making it invaluable for testing web applications.

- Capture and Logging: Burp Suite captures and logs requests made through the proxy by default, even when the interception is turned off. This logging functionality can be helpful for later analysis and review of prior requests.

- WebSocket Support: Burp Suite also captures and logs WebSocket communication, providing additional assistance when analysing web applications.

- Logs and History: The captured requests can be viewed in the HTTP history and WebSockets history sub-tabs, allowing for retrospective analysis and sending the requests to other Burp modules as needed.

- Response Interception: By default, the proxy does not intercept server responses unless explicitly requested on a per-request basis. The "Intercept responses based on the following rules" checkbox, along with the defined rules, allows for a more flexible response interception.

- Match and Replace: The "Match and Replace" section in the Proxy settings enables the use of regular expressions (regex) to modify incoming and outgoing requests. This feature allows for dynamic changes, such as modifying the user agent or manipulating cookies.


# Connecting through the Proxy (FoxyProxy)


Here are the steps to configure the Burp Suite Proxy with FoxyProxy:

1. Install FoxyProxy: Download and install the FoxyProxy Basic extension.

2. Access FoxyProxy Options: Once installed, a button will appear at the top right of the Firefox browser. Click on the FoxyProxy button to access the FoxyProxy options pop-up.

3. Create Burp Proxy Configuration: In the FoxyProxy options pop-up, click the Options button. This will open a new browser tab with the FoxyProxy configurations. Click the Add button to create a new proxy configuration.

4. Add Proxy Details: On the "Add Proxy" page, fill in the following values:

Title: Burp (or any preferred name)
Proxy IP: 127.0.0.1
Port: 8080

5. Save Configuration: Click Save to save the Burp Proxy configuration.

6. Activate Proxy Configuration: Click on the FoxyProxy icon at the top-right of the Firefox browser and select the Burp configuration. This will redirect your browser traffic through 127.0.0.1:8080. Note that Burp Suite must be running for your browser to make requests when this configuration is activated.

7. Enable Proxy Intercept in Burp Suite: Switch to Burp Suite and ensure that Intercept is turned on in the Proxy tab.

8. Download the CA Certificate: With the Burp Proxy activated, navigate to http://burp/cert. This will download a file called cacert.der. Save this file somewhere on your machine.

9. Access Firefox Certificate Settings: Type about:preferences into your Firefox URL bar and press Enter. This will take you to the Firefox settings page. Search the page for "certificates" and click on the View Certificates button.

10. Import the CA Certificate: In the Certificate Manager window, click on the Import button. Select the cacert.der file that you downloaded in the previous step.

11. Set Trust for the CA Certificate: In the subsequent window that appears, check the box that says "Trust this CA to identify websites" and click OK.

12. Test the Proxy: Open Firefox and try accessing a website, such as the homepage for http://MACHINE_IP/. Your browser will hang, and the proxy will populate with the HTTP request. Congratulations, you have successfully intercepted your first request!

# Site Map and Issue Definitions

The Target tab in Burp Suite provides more than just control over the scope of our testing. It consists of three sub-tabs:

- Site map: This sub-tab allows us to map out the web applications we are targeting in a tree structure. Every page that we visit while the proxy is active will be displayed on the site map. This feature enables us to automatically generate a site map by simply browsing the web application. In Burp Suite Professional, we can also use the site map to perform automated crawling of the target, exploring links between pages and mapping out as much of the site as possible. Even with Burp Suite Community, we can still utilize the site map to accumulate data during our initial enumeration steps. It is particularly useful for mapping out APIs, as any API endpoints accessed by the web application will be captured in the site map.

- Issue definitions: Although Burp Community does not include the full vulnerability scanning functionality available in Burp Suite Professional, we still have access to a list of all the vulnerabilities that the scanner looks for. The Issue definitions section provides an extensive list of web vulnerabilities, complete with descriptions and references. This resource can be valuable for referencing vulnerabilities in reports or assisting in describing a particular vulnerability that may have been identified during manual testing.

- Scope settings: This setting allows us to control the target scope in Burp Suite. It enables us to include or exclude specific domains/IPs to define the scope of our testing. By managing the scope, we can focus on the web applications we are specifically targeting and avoid capturing unnecessary traffic.






