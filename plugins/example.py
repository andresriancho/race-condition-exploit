import logging


class example(object):
    """
    Just an example, useful for documentation
    """
    def get_host(self):
        """
        :return: The domain/IP address to connect to
        """
        return 'www.paypal.com'

    def get_port(self):
        """
        :return: The port (as integer) to connect to
        """
        return 443

    def use_ssl(self):
        """
        :return: True if we should use SSL to send the request
        """
        return True

    def get_request_str(self):
        """
        :return: The HTTP request to send as a string. Remember, it should be
                 a complete request (with the trailing \n\r if GET) and returned
                 as a string.

                 This request will be sent as-is by the threads, without any
                 modification.

                 The threads will send all the request but the last byte to the
                 remote end, and when all threads are ready the last byte of
                 all requests will be sent

                 Recommendations:
                    * Make sure you respect the HTTP protocol, send \r\n not \n
                    * Accept-Encoding: identity
                    * Connection: close
        """
        return ''

    def analyze_response(self, response_str):
        """
        After sending the request, we retrieve the response and send it to this
        method where the goal is to analyze it and (if possible) tell if the
        request/exploit was successful

        :param response_str: A string with the HTTP response
        :return: None, logging is used
        """
        pass

    def end(self):
        """
        Called when all the process ends, useful for printing status, closing files, etc.
        :return: None
        """
        pass