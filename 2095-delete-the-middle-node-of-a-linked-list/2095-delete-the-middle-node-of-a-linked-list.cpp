/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* deleteMiddle(ListNode* head) {
        int size=0;
        ListNode*current=head;
        while(current){
            size++;current=current->next;
        }
        if(size==1)return NULL;
        size/=2;
        current=head;
        for(int i=1;i<size;i++){
            current=current->next;
        }
        current->next=current->next->next;
        return head;
    }
};