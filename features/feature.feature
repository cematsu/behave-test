Feature:  test

@test
  Scenario: abc123
    Given I create an access token
    When I send a GET request
    Then I receive a "200" status code