*** Settings ***
Documentation    testing apis related to users
...             register, login_in, get_user_info and so on
Resource    ../Keywords.resource
Suite Setup     Hello
Suite Teardown  Done
Default Tags    positive

*** Test Cases ***

test two number adding
    [Tags]    Demo
    log    "Hello, RF"  warn
    ${num}=  Evaluate    12+13
    Warn     result is ${num}
    Should Be Equal    ${num}  ${2}

test two number multiply
    [Tags]    robot:skip
    log   the second case
    ${num}=  Evaluate    12*12
    Should Be Equal    ${num}  ${144}

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