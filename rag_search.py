import java.util.ArrayList;
import java.util.List;

public class RAGDocumentSearch {
    private List<String> documents;

    public RAGDocumentSearch() {
        this.documents = new ArrayList<>();
    }

    public void addDocument(String document) {
        documents.add(document);
    }

    public List<String> getDocuments() {
        return documents;
    }

    public static void main(String[] args) {
        RAGDocumentSearch rag = new RAGDocumentSearch();
        rag.addDocument("This is a sample document.");
        rag.addDocument("This is another example document.");

        for (String doc : rag.getDocuments()) {
            System.out.println(doc);
        }
    }
}