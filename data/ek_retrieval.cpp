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
    {
        return response.extract_string();
    })
    .then([](std::string body)
    {
        std::cout << body << std::endl;
    });
}

int main()
{
    HTTPGetAsync().wait();
    return 0;
}
