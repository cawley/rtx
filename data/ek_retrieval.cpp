/*

RESTAPI SKELETON FOR REFINITIV CONTACT
FIRST WE SENT a GET request to the Eikon Data API and prints out the response.

NEXT STEPS:
implement a way to parse the JSON response to extract the data you want and then save that data to a .csv file.

for parsing JSON in C++: nlohmann/json, RapidJSON, JsonCpp

CPP REST SDK: for client-server comms with modern api design, by creating http clients and servers

HTTP client and server functionality.
JSON object model similar to the .NET JSON object model.
URI manipulation APIs.
Asynchronous streams.
Asynchronous task model, to avoid blocking network operations.

*/

#include <cpprest/http_client.h>
#include <cpprest/filestream.h>

using namespace utility;
using namespace web;
using namespace web::http;
using namespace web::http::client;
using namespace concurrency::streams;

pplx::task<void> HTTPGetAsync()
{
    http_client client(U("https://api.refinitiv.com/data/price/v1/views/summaries/US10YT=RR"));

    http_request req(methods::GET);
    req.headers().add(U("Authorization"), U("Bearer YOUR_ACCESS_TOKEN"));
    req.headers().add(U("Content-Type"), U("application/json"));

    return client.request(req).then([](http_response response)
                                    { return response.extract_string(); })
        .then([](std::string body)
              { std::cout << body << std::endl; });
}

int main()
{
    HTTPGetAsync().wait();
    return 0;
}
