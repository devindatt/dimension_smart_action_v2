
temp_log_items = [
        "Found a potential memory leak in the data processing module.",
        "Implemented a new caching mechanism for the API calls.",
        "Need feedback on the error handling approach in the latest commit.",
        "Updated the database schema, please check for integration issues.",
        "Refactored the authentication service for better security.",
        "Encountered a race condition in the multithreading implementation.",
        "Added unit tests for the newly developed features.",
        "Looking into the performance bottleneck in the image processing algorithm.",
        "Fixed a bug in the payment gateway integration.",
        "Exploring a new library for the front-end UI animations."
    ]


possible_outputs = ['code bug', 'compatiblity', 'complexity', 'process', 'UI/UX experience', 'security', 'compliance', 'performance', 'scope change', 'documentation', 'QA testing', 'create issue on Project Management'  ]


possible_categories = ['IDEs','Version Control Systems', 'Code Collaboration', 'CI/CD Tools', 'Project Management Tools', 'Containerization and Orchestration', 'Configuration Management Tools', 'Database Management Tools','Cloud Services', 'Testing Tools', 'Code Quality and Review Tools', 'Monitoring and Performance Tools', 'Documentation Tools', 'UI/UX Design Tools', 'Source Code Editors', 'Collaboration Tools','Security Tools']


possible_tools = '''
    'IDEs' =['Visual Studio','Eclipse', 'IntelliJ IDEA', 'PyCharm', 'Xcode', 'NetBeans', 'Android Studio', 'Visual Studio Code', 'Sublime Text', 'Atom']
    
    'Version Control Systems' =['Git', 'Mercurial', 'Concurrent Versions System']
    
    'Code Collaboration'= ['GitHub', 'GitLab', 'Bitbucket', 'Phabricator', 'Review Board', 'Gerrit']
    
    'CI/CD Tools'=['Jenkins', 'Travis CI', 'CircleCI', 'GitLab CI', 'Bamboo', 'TeamCity', 'Azure Pipelines']
    
    'Project Management Tools'=['Jira', 'Trello', 'Asana', 'Monday.com', 'Basecamp', 'ClickUp', 'Wrike']
    
    'Containerization and Orchestration'=['Docker', 'Kubernetes','Rancher', 'OpenShift']
    
    'Configuration Management Tools'=[Ansible', 'Chef','Puppet', 'Terraform', 'SaltStack']
    
    'Database Management Tools'=['MySQL Workbench', 'phpMyAdmin','MongoDB Compass','Navicat','DataGrip']
    
    'Cloud Services'=['Amazon Web Services', 'Microsoft Azure','Google Cloud Platform', 'Heroku', 'DigitalOcean']
    
    'Testing Tools'=['Selenium','Jest','Mocha', 'JUnit','TestRail', 'SoapUI','Postman','Cypress']
    
    'Code Quality and Review Tools'=['SonarQube','ESLint','Pylint','RuboCop','StyleCop']
    
    'Monitoring and Performance Tools'=['New Relic','Datadog','AppDynamics','Splunk','Grafana']
    
    'Documentation Tools'=['Confluence','Docusaurus','Sphinx','Swagger']
    
    'UI/UX Design Tools'=['Sketch','Adobe XD','Figma','InVision','Axure RP']
    
    'Source Code Editors'=['Visual Studio Code','Sublime Text','Atom','Vim']
    
    'Collaboration Tools'=['Slack','Microsoft Teams','Zoom','Discord','Trello']
    
    'Security Tools'=['Fortify','Checkmarx','OWASP ZAP','Burp Suite','Nessus']
    '''



template1 = '''You are an experienced application code developer. You are a knowledgeable in collaborating with teams to set specifications, write high-quality code, conduct testing, and troubleshoot applications. Please read the following log item {log_item} and choose the best classification from this list of possibilities {possible_outputs}. Note, you can only choose one classification. Be concise and only reply with one answer and no explanation. Also, if you can't make a determination from the list provided, please only reply with 'No category found!' '''    


template2 = '''You are an experienced application code developer. You are a knowledgeable about all the issues that might affect teams with collaboration to set specifications, write high-quality code, conduct testing, and troubleshoot applications. I will provide you a specfic outcome of possible software development issue {issue_item}. I want you to then choose the best possible tool category list from this possible category list {possible_categories} that is 'issue_item' belongs to. Be concise and only choose one item from the list. Then I want you to match that tool category from the 'possible_tools' list {possible_tools} is related to. Within that category list, I want you to randomly choose one of the tool items from that particular category list. Only reply with one tool answer in the following format with no explanation:

EXAMPLE OF OUTPUT:
Create item in 'Sphinx'

Note, if the 'issue_item' given is 'No category found!', then just reply with 'No action at this time.'
 '''    
