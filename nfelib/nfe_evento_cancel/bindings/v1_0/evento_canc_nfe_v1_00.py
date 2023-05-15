from dataclasses import dataclass
from nfelib.nfe_evento_cancel.bindings.v1_0.leiaute_evento_canc_nfe_v1_00 import Tevento

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


@dataclass
class Evento(Tevento):
    """
    Schema XML de validação do evento Cancelamento.
    """
    class Meta:
        name = "evento"
        namespace = "http://www.portalfiscal.inf.br/nfe"