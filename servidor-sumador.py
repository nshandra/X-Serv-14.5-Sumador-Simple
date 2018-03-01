#!/usr/bin/python3

import webapp
import calculadora


class servidor_sumador(webapp.webApp):
    usage = "Usage: hostname:port/operand1/function/operand2"

    def parse(self, request):
        input = str(request).split()[1].split('/')[1:]
        print(input)
        return input

    def process(self, parsedRequest):
        if '' in parsedRequest:
            output = self.usage
        else:
            try:
                output = calculadora.calculator(parsedRequest[1],
                                                parsedRequest[0],
                                                parsedRequest[2])
            except IndexError:
                output = self.usage
        print(output)

        return ("200 OK", "<html><head><meta charset='utf-8'>"
                "<h1>Calculadora webApp</h1></head>"
                "<body><p>" + str(output) + "</p></body></html>\r\n")


if __name__ == "__main__":
    testWebApp = servidor_sumador("localhost", 1234)
