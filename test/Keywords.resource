*** Settings ***
Documentation    this is a resource file, support cases
Library    ./library/ApiLibrary.py

*** Keywords ***
Hello
    Log    "Hello, Let's start"  warn

Done
    Log    "Thanks, Finished"  warn

Starting Test Api
    [Arguments]    ${user_tag}    ${host_tag}
    init_items_data     ${user_tag}    ${host_tag}
    Init Api


Verify single item valid
    [Arguments]    ${exact}   ${expect}
    Should Be Equal    ${exact}   ${expect}

Verify userinfo valid
    [Arguments]    ${result}    ${user_tag}
    ${user}=    Init User    ${user_tag}
    ${user}=    Get User Data
    Should Be Equal    ${user}[user_id]  ${result}[user_id]

    ${db}=      Connect To Mysql       mysql  user
    ${db}=      Query User   ${user}[user_id]
    warn  ${db}
    Should Be Equal    ${user}[name]  ${db}[1]
    Close Dbconnection

DB Verification
    [Arguments]    ${connect_info}  ${db}

Info
    [Arguments]    ${text}
    Log    ${text}  info

Warn
    [Arguments]    ${text}
    Log    ${text}  warn

Debug
    [Arguments]    ${text}
    Log    ${text}  debug