+elementos para o jsNotifications

#adicionar eventlistener ou hook para este evento
if ($RCMAIL->action == 'refresh') {
    $RCMAIL->plugins->exec_hook('refresh', array('last' => intval(rcube_utils::get_input_value('_last', rcube_utils::INPUT_GPC))));
}

#hook js
#~/skin/classic/function.js:1021
if (rcmail.gui_objects.mailboxlist) {
rcmail.treelist.addEventListener('expand', rcube_render_mailboxlist);
rcmail.addEventListener('responseaftermark', rcube_render_mailboxlist)
    .addEventListener('responseaftergetunread', rcube_render_mailboxlist)
====>.addEventListener('responseaftercheck-recent', rcube_render_mailboxlist)
    .addEventListener('responseafterrefresh', rcube_render_mailboxlist)
    .addEventListener('afterimport-messages', function(){ rcmail_ui.show_popup('uploadform', false); });
}
_task=mail&_action=refresh

"queryString": [
{
"name": "_task",
"value": "mail"
},
{
"name": "_action",
"value": "refresh"
}
],

no response a chave "exec": retorna isto ==>

this.set_unread_count("INBOX",969,true,"");this.set_quota({"used":428267,"total":10485760,"percent":4,"free":96,"type":"text","folder":"INBOX","title":"418 MB \/ 10 GB (4%)"});this.set_rowcount("Mensagens 1 - 50 de 1617","INBOX");this.message_list.clear(false);this.set_message_coltypes(["chbox","flag","fromto","threads","subject","date","attachment"],null,"from");

this.add_message_row(
7399,{
  "chbox":"<span id=\"msgicnrcmrowMTExOTg\" class=\"msgicon\" title=\"\"><\/span>\n<input type=\"checkbox\" name=\"rcmselect7399\" id=\"rcmselect7399\" \/><label for=\"rcmselect7399\" onclick=\"javascript:void(0);\"><span onclick=\"javascript:void(0);\"><\/span><\/label>",
  "fromto":"<span class=\"adr\"><span title=\"marcosptf@ymail.com\" class=\"rcmContactAddress\">Marcos Paulo<\/span><\/span>",
  "subject":"send notifications",
  "date":"Hoje 09:20"
},
{
"recent":1,"ctype":"multipart\/alternative","mbox":"INBOX"
},
false
);

this.add_message_row(7396,{"chbox":"<span id=\"msgicnrcmrowMTExOTg\" class=\"msgicon\" title=\"\"><\/span>\n        <input type=\"checkbox\" name=\"rcmselect7396\" id=\"rcmselect7396\" \/><label for=\"rcmselect7396\" onclick=\"javascript:void(0);\"><span onclick=\"javascript:void(0);\"><\/span><\/label>","fromto":"<span class=\"adr\"><span title=\"novo-webmail1@www539.locaweb.com.br\" class=\"rcmContactAddress\">novo-webmail1@www539.locaweb.com.br<\/span><\/span>","subject":"&quot;aaaaaaaaa&quot; confirmou presen\u00e7a por novo-webmail1@www539.locaweb.com.br","date":"Ter. 16:48"},{"seen":1,"ctype":"multipart\/alternative","mbox":"INBOX"},false);

this.add_message_row(7392,{"chbox":"<span id=\"msgicnrcmrowMTExOTg\" class=\"msgicon\" title=\"\"><\/span>\n        <input type=\"checkbox\" name=\"rcmselect7392\" id=\"rcmselect7392\" \/><label for=\"rcmselect7392\" onclick=\"javascript:void(0);\"><span onclick=\"javascript:void(0);\"><\/span><\/label>","fromto":"<span class=\"adr\"><span title=\"novo-webmail1@www539.locaweb.com.br\" class=\"rcmContactAddress\">novo-webmail1@www539.locaweb.com.br<\/span><\/span>","subject":"&quot;aaaaaaaaa&quot; confirmou presen\u00e7a por novo-webmail1@www539.locaweb.com.br","date":"Ter. 16:48"},{"seen":1,"ctype":"multipart\/alternative","mbox":"INBOX"},false);

this.add_message_row(7391,{"chbox":"<span id=\"msgicnrcmrowMTExOTg\" class=\"msgicon\" title=\"\"><\/span>\n        <input type=\"checkbox\" name=\"rcmselect7391\" id=\"rcmselect7391\" \/><label for=\"rcmselect7391\" onclick=\"javascript:void(0);\"><span onclick=\"javascript:void(0);\"><\/span><\/label>","fromto":"<span class=\"adr\"><span title=\"novo-webmail1@www539.locaweb.com.br\" class=\"rcmContactAddress\">novo-webmail1@www539.locaweb.com.br<\/span><\/span>","subject":"&quot;aaaaaaaaa&quot; confirmou presen\u00e7a por novo-webmail1@www539.locaweb.com.br","date":"Ter. 16:48"},{"seen":1,"ctype":"multipart\/alternative","mbox":"INBOX"},false);

this.add_message_row(7390,{"chbox":"<span id=\"msgicnrcmrowMTExOTg\" class=\"msgicon\" title=\"\"><\/span>\n        <input type=\"checkbox\" name=\"rcmselect7390\" id=\"rcmselect7390\" \/><label for=\"rcmselect7390\" onclick=\"javascript:void(0);\"><span onclick=\"javascript:void(0);\"><\/span><\/label>","fromto":"<span class=\"adr\"><span title=\"novo-webmail1@www539.locaweb.com.br\" class=\"rcmContactAddress\">novo-webmail1@www539.locaweb.com.br<\/span><\/span>","subject":"&quot;aaaaaaaaa&quot; confirmou presen\u00e7a por novo-webmail1@www539.locaweb.com.br","date":"Ter. 16:48"},{"seen":1,"ctype":"multipart\/alternative","mbox":"INBOX"},false);

this.add_message_row(7395,{"chbox":"<span id=\"msgicnrcmrowMTExOTg\" class=\"msgicon\" title=\"\"><\/span>\n        <input type=\"checkbox\" name=\"rcmselect7395\" id=\"rcmselect7395\" \/><label for=\"rcmselect7395\" onclick=\"javascript:void(0);\"><span onclick=\"javascript:void(0);\"><\/span><\/label>","fromto":"<span class=\"adr\"><span title=\"novo-webmail1@www539.locaweb.com.br\" class=\"rcmContactAddress\">novo-webmail1@www539.locaweb.com.br<\/span><\/span>","subject":"&quot;aaaaaaaaa&quot; confirmou presen\u00e7a por novo-webmail1@www539.locaweb.com.br","date":"Ter. 16:48"},{"ctype":"multipart\/alternative","mbox":"INBOX"},false);

