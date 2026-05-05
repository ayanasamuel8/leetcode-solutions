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
    ListNode* rotateRight(ListNode* head, int k) {
        ios::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);
        ListNode*left,*right,*end;
        left=right=end=head;
        int length=1;
        if(head==nullptr || head->next==nullptr||k==0) return head;


        while(end->next){
            end=end->next;
            length++;
        }
        end->next=head;
        k=length-(k%length);
        while((k--)-1){
                right=right->next;
        }
        head=right->next;
        right->next=nullptr;
        return head;
    }
};