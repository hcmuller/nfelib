"""This file was generated by xsdata, v24.2.1, on 2024-02-24 11:16:39

Generator: DataclassGenerator
See: https://xsdata.readthedocs.io/
"""
from dataclasses import dataclass
from nfelib.mdfe.bindings.v3_0.cons_reci_mdfe_tipos_basico_v3_00 import (
    TretConsReciMdfe,
)

__NAMESPACE__ = "http://www.portalfiscal.inf.br/mdfe"


@dataclass
class RetConsReciMdfe(TretConsReciMdfe):
    """
    Schema XML de validação do retorno do Pedido de Consulta do MDF-e.
    """

    class Meta:
        name = "retConsReciMDFe"
        namespace = "http://www.portalfiscal.inf.br/mdfe"
