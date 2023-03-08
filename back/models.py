from django.db import models
from simple_history.models import HistoricalRecords

#________________________________
#from .camada import Camada
#from .classe import Classe
#from .relevancia import Relevancia
#from .contrato import Contrato
#from .item_configuracao_responsavel import ItemConfiguracaoResponsavel
#________________________________
#__________contrato
class Contrato(models.Model):
    """
        o campo "tp_regra_cobranca", pode receber valor 'ic_porcentagem' ou 'ic_dia_faturar'

        ic_porcentagem => regra por %
        ic_dia_faturar => regra por dias (default)

        o campo "tp_relevancia", pode receber valor 'individual' ou 'grupo'

        individual => relevancia individual por IC`s
        grupo => relevancia por grupo do IC`s  (default)

    """
    id = models.IntegerField(primary_key=True)
    no_entidade = models.CharField(max_length=150, null=False)
    no_contrato = models.CharField(max_length=150, null=False)
    vl_unidade_servico = models.DecimalField(
        max_digits=12, decimal_places=2, null=False)
    nu_dia_faturamento = models.CharField(max_length=2, null=False)
    tp_regra_cobranca = models.CharField(
        max_length=14, default='ic_dia_faturar', null=False)
    tp_relevancia = models.CharField(
        max_length=10, default='grupo', null=False)
    bo_ativo = models.BooleanField(default=True, null=False)
    dt_sincronizacao = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords(
        table_name='historico\".\"contrato_history')

    class Meta:
        app_label = 'back'
        db_table = 'cliente\".\"contrato'
        indexes = [
            models.Index(fields=['id'], name='c_ctr_id_idx'),
            models.Index(fields=['no_entidade'], name='c_ctr_no_entidade_idx'),
            models.Index(fields=['no_contrato'], name='c_ctr_no_contrato_idx'),
            models.Index(fields=['tp_regra_cobranca'],
                         name='c_ctr_tp_rg_cbr_idx'),
            models.Index(fields=['tp_relevancia'], name='c_ctr_tp_rlvc_idx'),
            models.Index(fields=['vl_unidade_servico'],
                         name='c_ctr_vl_unidade_servico_idx'),
            models.Index(fields=['nu_dia_faturamento'],
                         name='c_ctr_nu_dia_faturamento_idx'),
            models.Index(fields=['bo_ativo'], name='c_ctr_bo_ativo_idx'),
            models.Index(fields=['dt_sincronizacao'],
                         name='c_ctr_dt_szc_idx'),
        ]

#from .contrato import Contrato
#__________camada

class Camada(models.Model):
    id = models.IntegerField(primary_key=True)
    contrato = models.ForeignKey(
        Contrato, related_name='CamadaContrato', on_delete=models.PROTECT)
    no_camada = models.CharField(max_length=100, null=False)
    bo_ativo = models.BooleanField(default=False, null=False)
    dt_sincronizacao = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords(
        table_name='historico\".\"camada_history')

    class Meta:
        app_label = 'back'
        db_table = 'cliente\".\"camada'
        indexes = [
            models.Index(fields=['id'], name='c_cmd_id_idx'),
            models.Index(fields=['no_camada'], name='c_cmd_no_camada_idx'),
            models.Index(fields=['bo_ativo'], name='c_cmd_bo_ativo_idx'),
            models.Index(fields=['dt_sincronizacao'],
                         name='c_cmd_dt_szc_idx'),
        ]
#__________classe
class Classe(models.Model):
    id = models.IntegerField(primary_key=True)
    contrato = models.ForeignKey(
        Contrato, related_name='ClasseContrato', on_delete=models.PROTECT)
    no_classe = models.CharField(max_length=100, null=False)
    no_descricao = models.CharField(max_length=100, null=False)
    ds_tag = models.CharField(max_length=100, null=False)
    bo_manual = models.BooleanField(default=False, null=False)
    bo_ativo = models.BooleanField(default=False, null=False)
    dt_sincronizacao = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords(
        table_name='historico\".\"classe_history')

    class Meta:
        app_label = 'back'
        db_table = 'cliente\".\"classe'
        indexes = [
            models.Index(fields=['id'], name='c_cls_id_idx'),
            models.Index(fields=['no_classe'], name='c_cls_no_classe_idx'),
            models.Index(fields=['no_descricao'],
                         name='c_cls_no_descricao_idx'),
            models.Index(fields=['ds_tag'], name='c_cls_ds_tag_idx'),
            models.Index(fields=['bo_manual'], name='c_cls_bo_manual_idx'),
            models.Index(fields=['bo_ativo'], name='c_cls_bo_ativo_idx'),
            models.Index(fields=['dt_sincronizacao'], name='c_cls_dt_szc_idx'),
        ]

#__________Relevancia
class Relevancia(models.Model):
    id = models.IntegerField(primary_key=True)
    contrato = models.ForeignKey(
        Contrato, related_name='RelevanciaContrato', on_delete=models.PROTECT)
    nu_relevancia = models.IntegerField(null=False)
    vl_percentual = models.DecimalField(
        max_digits=12, decimal_places=2, null=False)
    ds_relevancia = models.CharField(max_length=80, null=True, blank=True)
    dt_sincronizacao = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords(
        table_name='historico\".\"relevancia_history')

    class Meta:
        app_label = 'back'
        db_table = 'cliente\".\"relevancia'
        indexes = [
            models.Index(fields=['id'], name='c_rlc_id_idx'),
            models.Index(fields=['nu_relevancia'],
                         name='c_rlc_nu_relevancia_idx'),
            models.Index(fields=['vl_percentual'],
                         name='c_rlc_vl_percentual_idx'),
            models.Index(fields=['ds_relevancia'],
                         name='c_rlc_ds_relevancia_idx'),
            models.Index(fields=['dt_sincronizacao'], name='c_rlc_dt_szc_idx'),
        ]

#__________item_configuracao_responsavel
class ItemConfiguracaoResponsavel(models.Model):

    id = models.AutoField(primary_key=True)
    no_responsavel = models.CharField(max_length=150, null=False)
    dt_alteracao = models.DateTimeField(auto_now=True, null=True, blank=True)
    dt_cadastro = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords(
        table_name='historico\".\"item_configuracao_responsavel_history')

    class Meta:
        app_label = 'back'
        db_table = 'cliente\".\"item_configuracao_responsavel'
        indexes = [
            models.Index(fields=['id'],
                         name='c_itcgrpv_id_idx'),
            models.Index(fields=['no_responsavel'],
                         name='c_itcgrpv_no_responsavel_idx'),
        ]
#________________________________
class ItemConfiguracao(models.Model):
    """
        o campo "tp_regra_cobranca", pode receber valor 'ic_porcentagem' ou 'ic_dia_faturar'

        ic_porcentagem => regra por %
        ic_dia_faturar => regra por dias (default)

        o campo "tp_relevancia", pode receber valor 'individual' ou 'grupo'

        individual => relevancia individual por IC`s
        grupo => relevancia por grupo do IC`s  (default)

    """
    id = models.IntegerField(primary_key=True)
    contrato = models.ForeignKey(
        Contrato, related_name='ItemConfiguracaoContrato', on_delete=models.PROTECT)
    camada = models.ForeignKey(
        Camada, related_name='ItemConfiguracaoCamada', on_delete=models.PROTECT)
    classe = models.ForeignKey(
        Classe, related_name='ItemConfiguracaoClasse', on_delete=models.PROTECT)
    relevancia = models.ForeignKey(
        Relevancia, related_name='ItemConfiguracaoRelevancia', on_delete=models.PROTECT, null=True, blank=True)
    responsavel = models.ForeignKey(
        ItemConfiguracaoResponsavel, related_name='ItemConfiguracaoResponsavel', on_delete=models.PROTECT, null=True, blank=True)
    no_item = models.CharField(max_length=150, null=False)
    vl_item = models.DecimalField(
        max_digits=12, decimal_places=2, null=False)
    tp_regra_cobranca = models.CharField(
        max_length=14, default='ic_dia_faturar', null=False)
    tp_relevancia = models.CharField(
        max_length=10, default='grupo', null=False)
    nu_dia_regra_cobranca = models.IntegerField(null=True, blank=True)
    bo_rastreabilidade = models.BooleanField(default=False, null=False)
    bo_hibrido = models.BooleanField(default=False, null=False)
    dt_hibrido = models.DateField(null=True, blank=True)
    bo_ativo = models.BooleanField(default=False, null=False)
    dt_sincronizacao = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords(
        table_name='historico\".\"item_configuracao_history')

    class Meta:
        app_label = 'back'
        db_table = 'cliente\".\"item_configuracao'
        indexes = [
            models.Index(fields=['id'],
                         name='c_itcg_id_idx'),
            models.Index(fields=['no_item'],
                         name='c_itcg_no_item_idx'),
            models.Index(fields=['vl_item'],
                         name='c_itcg_vl_item_idx'),
            models.Index(fields=['nu_dia_regra_cobranca'],
                         name='c_itcg_n_d_r_c_idx'),
            models.Index(fields=['tp_regra_cobranca'],
                         name='c_itcg_t_rg_cr_idx'),
            models.Index(fields=['tp_relevancia'],
                         name='c_itcg_tp_rlvc_idx'),
            models.Index(fields=['bo_ativo'],
                         name='c_itcg_bo_ativo_idx'),
            models.Index(fields=['bo_rastreabilidade'],
                         name='c_itcg_bo_rastrea_idx'),
            models.Index(fields=['bo_hibrido'], name='c_itcg_bo_hibrido_idx'),
            models.Index(fields=['dt_hibrido'], name='c_itcg_dt_hibrido_idx'),
            models.Index(fields=['dt_sincronizacao'],
                         name='c_itcg_dt_szc_idx'),
        ]


