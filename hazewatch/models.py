from pydantic import BaseModel, Field, model_validator


class TopArea(BaseModel):
    latitude: float = Field(ge=-90, le=90)
    longitude: float = Field(ge=-180, le=180)
    count: int = Field(gt=0)
    
class HotspotMetrics(BaseModel):
    total: int = Field(ge=0)
    high_confidence: int = Field(ge=0)
    total_frp: float = Field(ge=0)
    top_area: TopArea | None
    trend: int | None
    
    @model_validator(mode="after")
    def validate_metrics(self):
        if self.high_confidence > self.total:
            raise ValueError(
                "high_confidence tidak boleh melibihi total"
            )
            
        if self.total == 0 and self.top_area is not None:
            raise ValueError(
                "top_area tidak boleh None jika ada hotspot"
            )
            
        if self.top_area is not None and self.top_area.count > self.total:
            raise ValueError(
                "Jumlah hotspot top_area tidak boleh melibihi total"
            )
            
        return self
    
    
    
    