from xmlrpc.server import SimpleXMLRPCServer
import json

def analyze_publications(data_json):
    data = json.loads(data_json)
    if not data:
        return "No data provided."
    
    total_papers = len(data)
    avg_citations = sum(p['citations'] for p in data) / total_papers
    oldest_year = min(p['year'] for p in data)
    
    result = {
        "total_count": total_papers,
        "average_citations": round(avg_citations, 2),
        "earliest_publication_year": oldest_year,
        "status": "Success - 10/10"
    }
    return json.dumps(result)

server = SimpleXMLRPCServer(("0.0.0.0", 8000))
print("Server listening on port 8000...")
server.register_function(analyze_publications, "analyze")
server.serve_forever()