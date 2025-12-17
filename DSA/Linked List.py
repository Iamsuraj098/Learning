# Linked List: 

class Node{
    Node next;
    int data;
    Node(){
        this.next = null;
    }
    Node(int data){
        this.data = data;
        this.next = null;
    }
    Node(int data, Node next){
        this.data = data;
        this.next = next;
    }
}
class Main {
    public static void main(String[] args) {
        Node head = null;
        Node last = null;
        for(int i=0;i<5;i++){
            Node temp = singlyLinkedList(i);
            if(head == null){
                head = temp;
                last = temp;
            }else{
	            last.next = temp;
                last = temp;
	        }
        }
        
        Node temp = head;
        int size = 0;
        while(temp.next != null){
            System.out.println(temp.data);
            temp = temp.next;
            size++;
        }
        
        // Middel element of the Linked List: 
        int[] arr = new int[size];
        int i = 0;
        temp = head;
        while(i != (size/2)){
            temp = temp.next;
            i++;
        }
        
        if(i == size/2){
            System.out.println("Mid Element: " + temp.data);
        }
        
        // Reverse a Linked List: 
        Node pre = null;
        Node curr = head;
        Node next = null;
        while(curr != null){
            pre = curr;
            curr = curr.next;
	    next = curr.next;
            curr.next = pre;
	    curr = next;
        }
        
    }
    
    static Node singlyLinkedList(int data){
        Node node = new Node();
        node.data = data;
        node.next = null;
        return node;
    }
}









