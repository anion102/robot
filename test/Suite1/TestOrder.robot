*** Settings ***
Documentation    testing apis related to users
...             register, login_in, get_user_info and so on
Resource    ../Keywords.resource
Default Tags    usr api
Suite Setup    Starting Test Api    ${USER}   ${HOST}

*** Variables ***
${USER}=    user1   # the user-key name in yaml file
${HOST}=    host1   # the host-key name in yaml file
*** Test Cases ***

test user register
    ${result}=  Register
    Warn     result is ${result}
    Should Be Equal    ${result}  ${123}

test user info
    ${result}=  Get User Information    user2
    Verify Userinfo Valid    ${result}  user2

test two number divide
    [Tags]    Demo
    Log    the third case
    ${num}=  Evaluate    24/12
    Should Be Equal    ${num}  ${2}
test two number minus
    [Tags]    Demo
    Log    the fourth case
    ${num}=  Evaluate    88-44
    Should Be Equal    ${num}  ${44}
