// Code generated by go-swagger; DO NOT EDIT.

package types

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"github.com/go-openapi/errors"
	"github.com/go-openapi/strfmt"
	"github.com/go-openapi/swag"
)

// SpotPricesHistoryReport spot prices history report
//
// swagger:model SpotPricesHistoryReport
type SpotPricesHistoryReport struct {

	// prices history
	PricesHistory *SpotPricesDatapoints `json:"prices_history,omitempty"`
}

// Validate validates this spot prices history report
func (m *SpotPricesHistoryReport) Validate(formats strfmt.Registry) error {
	var res []error

	if err := m.validatePricesHistory(formats); err != nil {
		res = append(res, err)
	}

	if len(res) > 0 {
		return errors.CompositeValidationError(res...)
	}
	return nil
}

func (m *SpotPricesHistoryReport) validatePricesHistory(formats strfmt.Registry) error {

	if swag.IsZero(m.PricesHistory) { // not required
		return nil
	}

	if m.PricesHistory != nil {
		if err := m.PricesHistory.Validate(formats); err != nil {
			if ve, ok := err.(*errors.Validation); ok {
				return ve.ValidateName("prices_history")
			}
			return err
		}
	}

	return nil
}

// MarshalBinary interface implementation
func (m *SpotPricesHistoryReport) MarshalBinary() ([]byte, error) {
	if m == nil {
		return nil, nil
	}
	return swag.WriteJSON(m)
}

// UnmarshalBinary interface implementation
func (m *SpotPricesHistoryReport) UnmarshalBinary(b []byte) error {
	var res SpotPricesHistoryReport
	if err := swag.ReadJSON(b, &res); err != nil {
		return err
	}
	*m = res
	return nil
}