"""This file was generated by xsdata, v24.2.1, on 2024-06-19 02:21:41

Generator: DataclassGenerator
See: https://xsdata.readthedocs.io/
"""

from dataclasses import dataclass
from nfelib.nfe.bindings.v4_0.leiaute_nfe_v4_00 import TretConsReciNfe

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


@dataclass
class RetConsReciNfe(TretConsReciNfe):
    """
    Schema XML de validação do retorno do Pedido de  Consulta do Recido do Lote de
    Notas Fiscais Eletrônicas.
    """

    class Meta:
        name = "retConsReciNFe"
        namespace = "http://www.portalfiscal.inf.br/nfe"
